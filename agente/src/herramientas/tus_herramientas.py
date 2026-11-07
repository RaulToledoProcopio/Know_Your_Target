"""Herramientas iniciales de reconocimiento. AQUÍ PUEDES AÑADIR LAS TUYAS.

WHOIS (whois.py), DNS y crt.sh ya están implementadas y activas en lanzar.py.
DNS y crt.sh proceden de la solución del profesor (herramientas/recon.py).

Para ampliar: una tarea por función, @protegida, sin shell, con timeout,
salida recortada, errores como texto y resultados filtrados por el alcance.
Importa tu nueva función en lanzar.py y añádela a HERRAMIENTAS.

Ideas: subdominios_subfinder, wayback_urls, correos (theHarvester / hunter.io),
infraestructura_ip, correo_postura (SPF/DMARC/MTA-STS/CAA), urlscan, shodan_host.
"""

import json
import subprocess
import urllib.parse
import urllib.request

from guard import protegida, filtrar
from whois import recortar

UA = "aap-recon/1.0 (educativo; IES Rafael Alberti)"
TIPOS_DNS = {"A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"}


def _http(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


@protegida(objetivo="dominio")
def dns_registros(dominio: str, tipo: str = "A") -> str:
    """Consulta registros DNS de un dominio. tipo: A, AAAA, MX, NS, TXT, CNAME o SOA.
    Devuelve los valores, uno por línea."""
    tipo = tipo.upper()
    if tipo not in TIPOS_DNS:
        return f"ERROR: tipo DNS no válido ({tipo}). Usa uno de: {', '.join(sorted(TIPOS_DNS))}."
    try:
        r = subprocess.run(["dig", "+short", tipo, dominio],
                           capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return "ERROR: dig no respondió en 20 segundos."
    except OSError as e:
        return recortar(f"ERROR: no se pudo ejecutar dig: {e}")
    if r.returncode != 0:
        return recortar(f"ERROR: dig falló ({r.returncode}): {r.stderr.strip() or 'sin detalles'}")
    salida = recortar(r.stdout.strip())
    return salida or f"Sin registros {tipo} para {dominio}."


@protegida(objetivo="dominio")
def subdominios_crtsh(dominio: str) -> str:
    """Enumera subdominios de un dominio por transparencia de certificados (crt.sh).
    Pasivo: no toca el objetivo. Devuelve solo los subdominios dentro del alcance."""
    url = f"https://crt.sh/?q=%25.{urllib.parse.quote(dominio)}&output=json"
    try:
        datos = json.loads(_http(url, timeout=90))
    except Exception as e:
        return (f"ERROR: crt.sh no respondió ({e}). crt.sh suele ir lento; "
                "puedes reintentar más tarde o añadir otra fuente de subdominios.")
    if not isinstance(datos, list) or any(
        not isinstance(fila, dict) or not isinstance(fila.get("name_value"), str)
        for fila in datos
    ):
        return "ERROR: crt.sh devolvió un formato de certificados inesperado."
    nombres = set()
    for fila in datos:
        for n in str(fila.get("name_value", "")).splitlines():
            n = n.strip().lstrip("*.").lower()
            if n:
                nombres.add(n)
    dentro, fuera = filtrar(sorted(nombres))
    cab = f"{len(dentro)} subdominios en alcance ({fuera} filtrados por estar fuera):\n"
    return recortar(cab + "\n".join(dentro))
@protegida(objetivo="dominio")
def cabeceras_http(dominio: str) -> str:
    """Comprueba las cabeceras HTTP de seguridad de un dominio autorizado."""

    url = f"https://{dominio}/"

    cabeceras_seguridad = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": UA},
            method="HEAD"
        )

        with urllib.request.urlopen(req, timeout=10) as respuesta:
            cabeceras = respuesta.headers

        resultado = [
            f"Análisis de cabeceras HTTP: {dominio}",
            f"Código HTTP: {respuesta.status}",
            ""
        ]

        for cabecera in cabeceras_seguridad:
            if cabeceras.get(cabecera):
                resultado.append(f"[OK] {cabecera}: {cabeceras.get(cabecera)}")
            else:
                resultado.append(f"[FALTA] {cabecera}")

        return "\n".join(resultado)

    except Exception as e:
        return f"ERROR consultando {dominio}: {e}"

@protegida(objetivo="dominio")
def robots_security(dominio: str) -> str:
    """Consulta robots.txt y security.txt de un dominio autorizado.
    Devuelve su contenido si están disponibles, sin seguir las rutas."""
    rutas = {
        "robots.txt": f"https://{dominio}/robots.txt",
        "security.txt": f"https://{dominio}/.well-known/security.txt",
    }

    resultados = [f"Ficheros públicos de {dominio}:"]

    for nombre, url in rutas.items():
        resultados.append(f"\n--- {nombre} ---")

        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": UA}
            )

            with urllib.request.urlopen(req, timeout=10) as respuesta:
                contenido = respuesta.read(8193)
                if len(contenido) > 8192:
                    contenido = contenido[:8192]
                    resultados.append("[Contenido truncado a 8 KB]")

                texto = contenido.decode("utf-8", "replace").strip()
                resultados.append(texto or "[Fichero vacío]")

        except urllib.error.HTTPError as e:
            if e.code == 404:
                resultados.append("[No encontrado: HTTP 404]")
            else:
                resultados.append(f"[ERROR HTTP {e.code}]")

        except Exception as e:
            resultados.append(f"[ERROR de consulta: {e}]")

    return recortar("\n".join(resultados))
@protegida(objetivo="dominio")
def netcraft_info(dominio: str) -> str:
    """Consulta el informe público de Netcraft para un dominio autorizado.
    Extrae información pública de hosting, red, DNS y registro del dominio."""
    from html.parser import HTMLParser

    class TablaNetcraft(HTMLParser):
        def __init__(self):
            super().__init__()
            self.fila = []
            self.celda = None
            self.datos = {}

        def handle_starttag(self, tag, attrs):
            if tag == "tr":
                self.fila = []
            elif tag in ("th", "td"):
                self.celda = []

        def handle_data(self, data):
            if self.celda is not None:
                self.celda.append(data)

        def handle_endtag(self, tag):
            if tag in ("th", "td") and self.celda is not None:
                texto = " ".join(" ".join(self.celda).split())
                self.fila.append(texto)
                self.celda = None
            elif tag == "tr" and len(self.fila) >= 2:
                self.datos[self.fila[0]] = self.fila[1]

    url = (
        "https://sitereport.netcraft.com/?url="
        + urllib.parse.quote(f"https://{dominio}", safe="")
    )

    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})

        with urllib.request.urlopen(req, timeout=20) as respuesta:
            contenido = respuesta.read(100001)

        if len(contenido) > 100000:
            return "ERROR: el informe de Netcraft supera el límite de 100 KB."

        parser = TablaNetcraft()
        parser.feed(contenido.decode("utf-8", "replace"))

        campos = [
            "Site title",
            "Site rank",
            "Description",
            "Date first seen",
            "Primary language",
            "Netblock Owner",
            "Hosting company",
            "Hosting country",
            "IPv4 address",
            "IPv4 autonomous systems",
            "IPv6 address",
            "IPv6 autonomous systems",
            "Reverse DNS",
            "Domain registrar",
            "Nameserver",
            "Nameserver organisation",
            "Organisation",
            "DNS admin",
            "DNS Security Extensions",
        ]

        resultados = [f"Informe público de Netcraft: {dominio}"]

        encontrados = 0
        for campo in campos:
            valor = parser.datos.get(campo)
            if valor:
                resultados.append(f"{campo}: {valor}")
                encontrados += 1

        if not encontrados:
            return (
                "ERROR: Netcraft respondió, pero no se pudieron extraer "
                "los campos esperados. Puede haber cambiado el formato."
            )

        resultados.append(
            "\nNota: la sección Site Technology no se incluye "
            "porque su contenido se carga dinámicamente."
        )

        return recortar("\n".join(resultados))

    except Exception as e:
        return recortar(f"ERROR consultando Netcraft para {dominio}: {e}")
