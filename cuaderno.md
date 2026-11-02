# Cuaderno de trabajo – Ubisoft

**Proyecto:** Know Your Target  
**Organización:** Ubisoft  
**Programa:** Ubisoft Responsible Disclosure Program  
**Plataforma:** Intigriti  

## Registro de reconocimiento pasivo

En este documento se registran cronológicamente las acciones realizadas durante el reconocimiento pasivo de Ubisoft.
Todas las consultas se realizarán utilizando fuentes públicasy respetando el alcance y las condiciones del programa.
Se documentarán la fecha, el objetivo, la herramienta utilizada, los resultados obtenidos y el siguiente paso de cada acción.

-----

## 1. Registro de acciones


### Acción 1 – WHOIS

> **Fecha:** 2026-11-02 17:00.
> **Objetivo:** `ubisoft.com` (dominio raíz; aplicación web pública de Ubisoft, incluida por la categoría general de activos web propiedad y operados por Ubisoft).
> **Herramienta:** Consulta WHOIS en https://www.whois.com/whois/ubisoft.com
> **Resultado:**
> - **Registrador:** Gandi SAS (IANA ID: 81).
> - **Fechas:** registro: 27/04/1995; última actualización: 13/10/2026; expiración: 28/04/2033.
> - **Servidores DNS:** `nic7.ubisoft.com`, `nic8.ubisoft.com`, `nic9.ubisoft.com`, `nic10.ubisoft.com`, `nic11.ubisoft.com` y `nic12.ubisoft.com`.
> - **Contactos:** WHOIS publica contactos de titularidad, administración, soporte técnico y abuso. Se omiten sus nombres y datos de contacto personales.
>
> **Siguiente paso:** Consultar los registros DNS (NS, MX y TXT) de `ubisoft.com`.

-----

### Acción 2 – Registros DNS

> **Fecha:** 2026-11-02 17:28.
> **Objetivo:** `ubisoft.com` (dominio raíz; aplicación web pública de Ubisoft, incluida por la categoría general de activos web propiedad y operados por Ubisoft).
> **Herramientas:** DNSDumpster (https://dnsdumpster.com/) y Google Admin Toolbox – Dig (https://toolbox.googleapps.com/apps/dig/).
> **Resultado:**
> - **Registros NS:** se identifican seis servidores DNS: `nic7.ubisoft.com` (193.108.91.206), `nic8.ubisoft.com` (84.53.139.65), `nic9.ubisoft.com` (184.26.161.66), `nic10.ubisoft.com` (95.100.175.67), `nic11.ubisoft.com` (2.16.40.64) y `nic12.ubisoft.com` (184.85.248.65). Están asociados a Akamai.
> - **Registros MX:** aparece `ubisoftaad.mail.protection.outlook.com`, con prioridad 10 e IP asociada 52.101.190.2, perteneciente a Microsoft.
> - **Registros TXT:** se encuentra el registro SPF `v=spf1 redirect=_spf.ubisoft.com`, además de registros de verificación de distintos servicios, entre ellos Google, Microsoft, Facebook, Apple, Atlassian, MongoDB, Miro, Bugcrowd, Anthropic, Yahoo, DocuSign y Docker.
> - **Registro DMARC:** mediante una consulta TXT específica a `_dmarc.ubisoft.com` se obtiene `v=DMARC1; p=reject; pct=100; rua=mailto:dmarcreport@ubisoft.com,mailto:dmarc_agg@vali.email;`. La política `reject` indica que los correos que no superen las comprobaciones DMARC deben rechazarse. Se aplica al 100 % de los correos sujetos a la política. Los informes agregados se envían a las dos direcciones indicadas. El TTL del registro es de una hora.
>
> **Siguiente paso:** Identificar subdominios de Ubisoft mediante Subfinder y crt.sh.

-----

### Acción 3 – Enumeración de subdominios

> **Fecha:** 2026-11-02. 18:25
>
> **Objetivo:** Enumerar los subdominios asociados a `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`, e identificar cuáles están dentro del alcance del programa Ubisoft Responsible Disclosure Program de Intigriti.
>
> **Herramientas:** Subfinder y crt.sh.
>
> **Qué hice:**
> - Ejecuté Subfinder sobre los tres dominios para recopilar nombres de subdominios.
> - Consulté crt.sh para obtener los nombres incluidos en los certificados TLS emitidos para esos dominios.
> - Comparé los nombres obtenidos con los patrones de alcance del programa: `*.ubisoft.com`, `*.ubi.com` y `*.ubisoftconnect.com`.
> - Comprobé las exclusiones expresas: `forums.ubisoft.com`, `ivalua.ubisoft.com` y `suppliers-ivalua.ubisoft.com`.
>
> **Resultado:**
>
> **1. Dominio `ubisoft.com`**
> - Subfinder obtuvo 15.684 nombres.
> - crt.sh proporcionó 1.531 nombres únicos, incluida la raíz `ubisoft.com`.
> - Los listados dieron 1.529 coincidencias, 2 nombres exclusivos de crt.sh y 14.155 exclusivos de Subfinder.
> - Algunos subdominios encontrados fueron:
>   - `chef-infra-server.ubisoft.com`
>   - `grafana.drp.avtr.ubisoft.com`
>   - `influxdb.live.avtr.ubisoft.com`
>   - `prod.scout.ubisoft.com`
>   - `maintenance.tu6.dev.avtr.ubisoft.com`
>
> **2. Dominio `ubi.com`**
> - Subfinder obtuvo un listado de 23.142 líneas.
> - crt.sh proporcionó un listado de 7.960 líneas.
> Algunos subdominios encontrados fueron:
  >    - `callofjuarez.es.ubi.com`
  >    - `cert-g2w-explore-acod.ubi.com`
  >    - `nexus.ubiservices.ubi.com`
  >    - `cert-manager3.dev.fleet.ubi.com`
  >    - `msr-api.aws-ubiservices.ubi.com`
  >    - `alertmanager.online-services.r6-playground.aws.r6.ubi.com`
  >    - `public.progression.ubisoftplus.webservices.dev.global.harbour.ubi.com`
  >    - `*.rocksmithmobile.ubi.com`
  >    - `*.live.admin.ksie-certmanz.test.fleet.ubi.com`
  >    - `*.live.public.ksie-certmanz.test.fleet.ubi.com`
  >    - `*.s2s.space03.experimental.bge2-dev.ubi.com`
  >    - `*.admin.space03.experimental.bge2-dev.ubi.com`
>
> **3. Dominio `ubisoftconnect.com`**
> - Subfinder obtuvo los siguientes 13 subdominios:
>   - `www.qr.ubisoftconnect.com`
>   - `www.emea.ubisoftconnect.com`
>   - `emea.ubisoftconnect.com`
>   - `www.cert2.ubisoftconnect.com`
>   - `wwwg.ubisoftconnect.com`
>   - `qrg.ubisoftconnect.com`
>   - `nz9iscvynlokyqwk4mgpqsg5em3fbfj1r8ldbxht.ubisoftconnect.com`
>   - `qr.ubisoftconnect.com`
>   - `www.ubisoftconnect.com`
>   - `dev.ubisoftconnect.com`
>   - `cert2.ubisoftconnect.com`
>   - `ncsa.ubisoftconnect.com`
>   - `www.ncsa.ubisoftconnect.com`
> - crt.sh mostró certificados para `ubisoftconnect.com`, `*.ubisoftconnect.com` y nombres concretos como `qr.ubisoftconnect.com`.
>
> **Evaluación del alcance:**
> - **Dentro del alcance:**
>   - Los dominios raíz `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`, por la categoría general de aplicaciones web públicas propiedad y operadas por Ubisoft.
>   - Los subdominios de `ubisoft.com` que pertenecen al patrón `*.ubisoft.com`, excepto los excluidos expresamente.
>   - Los subdominios de `ubi.com` que pertenecen al patrón `*.ubi.com`.
>   - Los subdominios de `ubisoftconnect.com` que pertenecen al patrón `*.ubisoftconnect.com`.
> - **Fuera del alcance:**
>   - `forums.ubisoft.com`
>   - `ivalua.ubisoft.com`
>   - `suppliers-ivalua.ubisoft.com`
>
> **Siguiente paso:** Análisis de huella tecnológica con Netcraft para identificar hosting, CDN/WAF, tecnologías e histórico.

-----

### Acción 4 – Huella tecnológica (Netcraft)

> **Fecha:** 2026-11-02. 18:47
>
> **Objetivo:** `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`.
>
> **Herramienta:** Netcraft Site Report ([https://sitereport.netcraft.com/](https://sitereport.netcraft.com/)).
>
> **Qué hice:**
> - Consulté los informes públicos de Netcraft para los tres dominios.
> - Revisé la información de red, alojamiento, servidores DNS, seguridad y tecnologías web detectadas.
> - Comparé los resultados para identificar similitudes y diferencias entre los dominios.
>
> **Resultados:**
>
> **1. `ubisoft.com`**
> - Hosting: Amazon.
> - País: Estados Unidos.
> - IP: `52.222.177.122`.
> - ASN: AS16509.
> - DNS inverso: `server-52-222-177-122.lhr95.r.cloudfront.net`.
> - Nameserver: `nic7.ubisoft.com`.
> - Registrador: Gandi.
> - DNSSEC: habilitado.
> - Tecnologías: AWS CloudFront, JavaScript, SSL, Gzip, CSP, HTML5 y CSS externo.
> - DMARC: `p=reject`, aplicado al 100 %.
> - No se identificó expresamente ningún WAF.
>
> **2. `ubi.com`**
> - Hosting: Amazon, centro de datos US East (Northern Virginia).
> - IP: `98.80.35.94`.
> - ASN: AS14618.
> - DNS inverso: `ec2-98-80-35-94.compute-1.amazonaws.com`.
> - Nameserver: `nic7.ubisoft.com`.
> - Registrador: Gandi.
> - DNSSEC: habilitado.
> - Tecnologías: AWS EC2, CloudFront, JavaScript, SSL, Gzip, CSP, HTML5 y CSS externo.
> - DMARC: `p=reject`, aplicado al 100 %.
> - No se identificó expresamente ningún WAF.
>
> **3. `ubisoftconnect.com`**
> - Hosting: Amazon, centro de datos US East (Northern Virginia).
> - IP: `3.228.105.175`.
> - ASN: AS14618.
> - DNS inverso: `ec2-3-228-105-175.compute-1.amazonaws.com`.
> - Nameserver: `ns1.gandi.net`.
> - Registrador: Gandi.
> - DNSSEC: habilitado.
> - Tecnologías: AWS CloudFront, EC2, Express.js, JavaScript, Google Hosted Libraries, SSL, Gzip, CSP, HTML5 y CSS externo.
> - SPF: incluye `_mailcust.gandi.net` y termina en `?all` (neutral).
> - DMARC: Netcraft indica que no se encontró un registro DMARC.
>
> **Conclusión:** La consulta permite identificar el uso de servicios de Amazon Web Services, especialmente CloudFront, en los tres dominios analizados. También se observan diferencias en sus direcciones IP, sistemas autónomos, servidores DNS y configuración del correo electrónico. Estos datos ayudan a conocer la infraestructura tecnológica visible públicamente, sin realizar pruebas activas sobre los sistemas.
>
> **Siguiente paso:** Consultar los ficheros públicos `robots.txt` y `security.txt` de los dominios seleccionados.

-----

### Acción 5 – Consulta de ficheros públicos (robots.txt y security.txt)

> **Fecha:** 2026-11-02 19:05
>
> **Objetivo:** `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`.
>
> **Herramienta:** Navegador web.
>
> **Qué hice:**
> - Consulté los ficheros `robots.txt` y `security.txt` de los tres dominios.
> - Comprobé también la variante `www` de `ubisoft.com`.
> - Revisé las respuestas obtenidas y las posibles redirecciones.
>
> **Resultados:**
>
> **1. `ubisoft.com`**
> - `robots.txt`: disponible.
> - Contiene cinco reglas `Disallow` que afectan a rutas de descargas, búsquedas y documentos de privacidad relacionados con procesos de selección.
> - Incluye el sitemap: `https://www.ubisoft.com/sitemap.xml`.
> - `security.txt`: devuelve `404 Not Found`.
> - La variante `https://www.ubisoft.com/.well-known/security.txt` también devuelve `404 Not Found`.
>
> **2. `ubi.com`**
> - Las consultas a `robots.txt` y `security.txt` redirigen a páginas de Ubisoft.
> - No se identificaron ficheros independientes mediante estas consultas.
>
> **3. `ubisoftconnect.com`**
> - Las consultas a `robots.txt` y `security.txt` redirigen a la página web de Ubisoft Connect.
> - No se identificaron ficheros independientes mediante estas consultas.
>
> **Conclusión:** Se localizó el fichero `robots.txt` de `ubisoft.com`, que contiene indicaciones para los rastreadores de buscadores sobre determinadas rutas que no se desean indexar. No se encontró `security.txt` en las direcciones comprobadas. Los otros dos dominios redirigieron a páginas de Ubisoft. La comprobación se realizó mediante consultas públicas, sin intentar acceder a rutas restringidas.
>
> **Siguiente paso:** Consultar los servicios expuestos mediante Shodan o InternetDB.

-----

### Acción 6 – Servicios expuestos (Shodan / InternetDB)

> **Fecha:** 2026-11-02. 19:25
>
> **Objetivo:** `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`.
>
> **Herramientas:** Shodan e InternetDB.
>
> **Qué hice:**
> - Consulté las direcciones IP obtenidas en el apartado 4 mediante InternetDB y Shodan.
> - Revisé los puertos y servicios identificados públicamente.
>
> **Resultados:**
>
> **1. `ubisoft.com` – `52.222.177.122`**
> - Puerto 80/tcp: HTTP (Amazon CloudFront).
> - Puerto 443/tcp: HTTPS (Shodan identifica Apache 2.4.68, aunque aparece contenido de un dominio ajeno).
>
> **2. `ubi.com` – `98.80.35.94`**
> - Puerto 80/tcp: HTTP (AWS Elastic Load Balancing).
> - Puerto 443/tcp: HTTPS (AWS Elastic Load Balancing).
>
> **3. `ubisoftconnect.com` – `3.228.105.175`**
> - Puerto 80/tcp: HTTP (AWS Elastic Load Balancing).
> - Puerto 443/tcp: HTTPS (AWS Elastic Load Balancing).
>
> **Siguiente paso:** Realizar búsquedas avanzadas mediante Google Dorks.

-----

### Acción 7 – Google Dorks

> **Fecha:** 2026-11-02. 19:52
>
> **Objetivo:** `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`.
>
> **Herramientas:** Google y Google Hacking Database (GHDB).
>
> **Qué hice:**
> - Realicé búsquedas avanzadas en Google mediante operadores `site:`, `filetype:`, `intitle:` e `inurl:`.
> - Comprobé la existencia de documentos, directorios y páginas de acceso indexados públicamente.
>
> **Resultados:**
> - `ubisoft.com`: se encontraron varios documentos PDF indexados públicamente.
> - `ubi.com`: se encontraron manuales de videojuegos y otros documentos PDF.
> - `patches.ubi.com`: se encontraron directorios públicos indexados con archivos de parches de videojuegos.
> - `ubisoftconnect.com`: no se encontraron resultados relevantes en las búsquedas realizadas.
> - Las búsquedas de archivos DOC/DOCX y páginas con `inurl:admin` o `inurl:login` no devolvieron resultados relevantes.
> - Google mostró un CAPTCHA durante una de las consultas, por lo que no se insistió.
>
> **Siguiente paso:** Buscar direcciones de correo electrónico asociadas a Ubisoft.

-----

### Acción 8 – Búsqueda de correos electrónicos

> **Fecha:** 2026-11-02. 20:25
>
> **Objetivo:** `ubisoft.com`.
>
> **Herramienta:** Hunter.io (Domain Search).
>
> **Qué hice:**
> - Consulté el dominio `ubisoft.com` mediante la función Domain Search de Hunter.io.
> - Revisé los correos electrónicos encontrados y su clasificación.
> - Los resultados aparecían divididos en tres categorías: People, Decision Maker y Generic.
> - La mayoría de las direcciones estaban ocultas y era necesario utilizar créditos (*coins*) de la plataforma para desbloquearlas.
> - Utilicé los 50 créditos disponibles para consultar contactos de la categoría Decision Maker.
>
> **Resultados:**
> - Hunter.io mostró aproximadamente 3.000 direcciones de correo asociadas a `ubisoft.com`.
> - Se recopilaron 47 contactos de la categoría Decision Maker.
> - Entre los cargos identificados había directores, responsables de tecnología, producción, comunicación, recursos humanos, asuntos legales, marketing y otros departamentos.
> - Entre los cargos identificados se encuentran CEO, Executive Director, General Manager, Managing Director, Chief Technology Officer, Head of Information Technology, Director de IT Strategy y Director Legal. Se omiten los nombres para no conservar datos personales.
> - Se observó que el patrón de correo más habitual es `nombre.apellido@ubisoft.com`.
> - También se observó alguna excepción al patrón, sin reproducir direcciones personales.
> - Algunas direcciones mostraban la opción de verificación (*Verify*), por lo que no se puede asegurar que todas estén verificadas.
> - Los resultados indicaban diferentes fuentes de procedencia para los contactos, algunas con más de 20 fuentes.
>
> **Conclusión:** Se obtuvo información pública sobre la estructura organizativa de Ubisoft y sus contactos profesionales. Se identificó un posible patrón de nomenclatura de correos corporativos, aunque existen excepciones. El acceso a las direcciones completas está limitado por el sistema de créditos de Hunter.io.
>
> **Siguiente paso:** Realización del mapa de superficie de ataque.