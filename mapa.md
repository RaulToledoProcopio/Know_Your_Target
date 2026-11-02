# Mapa de reconocimiento – Ubisoft

## 1. Resumen

Ubisoft es una empresa internacional dedicada al desarrollo y distribución de videojuegos. Durante el reconocimiento pasivo se analizaron los dominios `ubisoft.com`, `ubi.com` y `ubisoftconnect.com`, teniendo en cuenta el alcance publicado en su programa Responsible Disclosure de Intigriti [cuaderno, acciones 1–3].

Se identificó una infraestructura basada principalmente en Amazon Web Services (AWS), con tecnologías como CloudFront y Elastic Load Balancing, además de servicios DNS asociados a Akamai [cuaderno, acciones 2, 4 y 6].

También se encontraron configuraciones de correo vinculadas a Microsoft 365, documentos y directorios públicos indexados por buscadores y numerosos subdominios [cuaderno, acciones 2, 3 y 7].

Por último, Hunter.io mostró aproximadamente 3.000 direcciones asociadas a `ubisoft.com` y permitió recopilar 47 contactos de la categoría Decision Maker [cuaderno, acción 8].

## 2. Dominios y subdominios

Durante la enumeración se utilizaron Subfinder y crt.sh para identificar subdominios asociados a los tres dominios principales [cuaderno, acción 3].

| Dominio o subdominio | IP identificada | En alcance | Función aparente | Referencia al cuaderno |
|---|---|---|---|---|
| `ubisoft.com` | `52.222.177.122` | Sí, por la categoría general de aplicaciones web públicas propiedad y operadas por Ubisoft | Dominio principal de Ubisoft. | Acciones 3–4 |
| `ubi.com` | `98.80.35.94` | Sí, por la categoría general de aplicaciones web públicas propiedad y operadas por Ubisoft | Dominio utilizado por servicios y plataformas de Ubisoft. | Acciones 3–4 |
| `ubisoftconnect.com` | `3.228.105.175` | Sí, por la categoría general de aplicaciones web públicas propiedad y operadas por Ubisoft | Dominio asociado a Ubisoft Connect. | Acciones 3–4 |
| `chef-infra-server.ubisoft.com` | No identificada | Sí, según el patrón publicado | Posible infraestructura de gestión y configuración. | Acción 3 |
| `grafana.drp.avtr.ubisoft.com` | No identificada | Sí, según el patrón publicado | Posible panel de monitorización Grafana. | Acción 3 |
| `influxdb.live.avtr.ubisoft.com` | No identificada | Sí, según el patrón publicado | Posible servicio de almacenamiento de métricas. | Acción 3 |
| `prod.scout.ubisoft.com` | No identificada | Sí, según el patrón publicado | Posible servicio de producción interno. | Acción 3 |
| `maintenance.tu6.dev.avtr.ubisoft.com` | No identificada | Sí, según el patrón publicado | Posible entorno de desarrollo o mantenimiento. | Acción 3 |
| `nexus.ubiservices.ubi.com` | No identificada | Sí, según el patrón publicado | Posible servicio interno o de distribución. | Acción 3 |
| `msr-api.aws-ubiservices.ubi.com` | No identificada | Sí, según el patrón publicado | API asociada a servicios desplegados en AWS. | Acción 3 |
| `cert-manager3.dev.fleet.ubi.com` | No identificada | Sí, según el patrón publicado | Posible gestión de certificados en un entorno de desarrollo. | Acción 3 |
| `alertmanager.online-services.r6-playground.aws.r6.ubi.com` | No identificada | Sí, según el patrón publicado | Posible servicio de alertas y monitorización. | Acción 3 |
| `www.ubisoftconnect.com` | No identificada | Sí, según el patrón publicado | Sitio web de Ubisoft Connect. | Acción 3 |
| `dev.ubisoftconnect.com` | No identificada | Sí, según el patrón publicado | Posible entorno de desarrollo. | Acción 3 |
| `qr.ubisoftconnect.com` | No identificada | Sí, según el patrón publicado | Servicio relacionado con códigos QR. | Acción 3 |
| `www.qr.ubisoftconnect.com` | No identificada | Sí, según el patrón publicado | Posible acceso web al servicio de códigos QR. | Acción 3 |
| `emea.ubisoftconnect.com` | No identificada | Sí, según el patrón publicado | Servicio dirigido a la región EMEA. | Acción 3 |
| `cert2.ubisoftconnect.com` | No identificada | Sí, según el patrón publicado | Posible entorno de certificación. | Acción 3 |

Las referencias remiten a las acciones numeradas del cuaderno. Las funciones aparentes son inferencias a partir del nombre del subdominio, no servicios confirmados.

**Consideraciones sobre el alcance:**

- El programa Responsible Disclosure de Intigriti contempla los patrones `*.ubisoft.com`, `*.ubi.com` y `*.ubisoftconnect.com`.
- La política también incluye aplicaciones web públicas propiedad y operadas por Ubisoft. Los tres dominios raíz se consideran dentro del alcance por esta categoría general, no por asumir que los comodines los cubren.
- Se excluyen expresamente `forums.ubisoft.com`, `ivalua.ubisoft.com` y `suppliers-ivalua.ubisoft.com`.
- La inclusión de un subdominio debe confirmarse en las condiciones vigentes del programa antes de realizar cualquier prueba activa.
- Las IP indicadas para los dominios principales proceden del análisis de Netcraft. No se han atribuido IP a subdominios cuando no se dispone de ese dato.

## 3. Infraestructura y servicios

### 3.1. Hosting e infraestructura

El análisis de Netcraft permitió identificar infraestructura alojada principalmente en Amazon Web Services (AWS) [cuaderno, acción 4].

Las IP y la infraestructura de cada dominio en esta tabla se documentan en la acción 4 del cuaderno.

| Dominio | IP | Infraestructura identificada |
|---|---|---|
| `ubisoft.com` | `52.222.177.122` | Amazon CloudFront |
| `ubi.com` | `98.80.35.94` | Amazon EC2 y CloudFront |
| `ubisoftconnect.com` | `3.228.105.175` | Amazon EC2 y CloudFront |

También se identificaron los siguientes elementos:

- **Registrador:** Gandi.
- **Servidores de nombres observados:** `ubisoft.com` y `ubi.com` usan `nic7.ubisoft.com`, asociado a Akamai; para `ubisoftconnect.com`, Netcraft muestra `ns1.gandi.net`.
- DNSSEC habilitado en los tres dominios analizados según Netcraft.
- Uso de servicios de distribución de contenido mediante CloudFront.

### 3.2. Tecnologías identificadas

Netcraft mostró las siguientes tecnologías y características [cuaderno, acción 4]:

- JavaScript.
- SSL.
- Gzip.
- Content Security Policy (CSP).
- HTML5.
- Hojas de estilo externas.
- AWS CloudFront.
- AWS EC2.
- Express.js en `ubisoftconnect.com`.
- Google Hosted Libraries en `ubisoftconnect.com`.

No se identificó explícitamente un WAF en los resultados consultados de Netcraft.

### 3.3. DNS y correo electrónico

La consulta DNS permitió identificar los siguientes registros [cuaderno, acción 2]:

**Servidores DNS:**

- `nic7.ubisoft.com` – `193.108.91.206`
- `nic8.ubisoft.com` – `84.53.139.65`
- `nic9.ubisoft.com` – `184.26.161.66`
- `nic10.ubisoft.com` – `95.100.175.67`
- `nic11.ubisoft.com` – `2.16.40.64`
- `nic12.ubisoft.com` – `184.85.248.65`

Estos servidores aparecen asociados a Akamai.

**Correo electrónico:**

- Registro MX: `ubisoftaad.mail.protection.outlook.com`.
- Prioridad MX: 10.
- IP identificada: `52.101.190.2`.
- Servicio asociado: Microsoft.

El registro SPF encontrado fue:

`v=spf1 redirect=_spf.ubisoft.com`

El registro DMARC encontrado fue:

`v=DMARC1; p=reject; pct=100; rua=mailto:dmarcreport@ubisoft.com,mailto:dmarc_agg@vali.email;`

La política DMARC utiliza `p=reject` con un porcentaje del 100 %, lo que indica una política estricta frente a mensajes que no superen las comprobaciones de autenticación.

También se encontraron registros TXT de verificación asociados a servicios como Google, Microsoft, Facebook, Apple, Atlassian, MongoDB, Miro, Bugcrowd, Anthropic, Yahoo, DocuSign y Docker.

### 3.4. Servicios y archivos públicos

En la revisión de archivos públicos se encontraron los siguientes resultados [cuaderno, acción 5]:

- `ubisoft.com/robots.txt` está disponible y contiene reglas `Disallow` relacionadas con distintas rutas del sitio.
- Se identificó el sitemap `https://www.ubisoft.com/sitemap.xml`.
- No se encontró un archivo `security.txt` en las rutas comprobadas de `ubisoft.com`.
- Las consultas equivalentes en `ubi.com` y `ubisoftconnect.com` redirigieron a páginas de Ubisoft.

En las búsquedas de Google también se identificaron documentos PDF públicos, como manuales de videojuegos, informes, comunicados y documentación relacionada con Ubisoft [cuaderno, acción 7].

Además, se encontraron directorios públicos indexados en `patches.ubi.com` que contienen archivos de actualización de distintos videojuegos [cuaderno, acción 7].

### 3.5. Resultados de Shodan e InternetDB

La consulta de Shodan e InternetDB mostró los siguientes resultados [cuaderno, acción 6]:

| IP | Puertos identificados | Información |
|---|---|---|
| `52.222.177.122` | 80/tcp y 443/tcp | HTTP y HTTPS asociados a Amazon CloudFront. Shodan identifica Apache 2.4.68. |
| `98.80.35.94` | 80/tcp y 443/tcp | Servicios HTTP y HTTPS asociados a AWS Elastic Load Balancing. |
| `3.228.105.175` | 80/tcp y 443/tcp | Servicios HTTP y HTTPS asociados a AWS Elastic Load Balancing. |

En la IP `52.222.177.122` se observaron nombres de host y contenido relacionados con un dominio ajeno a Ubisoft. Por tanto, no se puede atribuir directamente ese servicio a Ubisoft.

En las otras dos IP se identificó un certificado TLS cuyo nombre común y nombres alternativos incluyen dominios de Ubisoft, entre ellos `ubisoft.com`, `*.ubisoft.com` y `*.ubi.com`.

InternetDB no mostró vulnerabilidades conocidas para las tres IP consultadas.

## 4. Correos y personas

La búsqueda realizada mediante Hunter.io sobre el dominio `ubisoft.com` mostró aproximadamente 3.000 direcciones de correo electrónico asociadas a la organización [cuaderno, acción 8].

Se utilizaron los créditos disponibles para consultar contactos de la categoría Decision Maker, recopilando 47 contactos [cuaderno, acción 8].

Entre los cargos y personas identificados destacan:

| Cargo identificado |
|---|
| CEO |
| Executive Director |
| General Manager |
| Managing Director |
| Chief Technology Officer |
| Head of Information Technology |
| Director de IT Strategy |
| Director Legal |

Se omiten los nombres y los datos de contacto personales; se conservan únicamente los cargos observados.

### Patrón de correo

El patrón de correo más frecuente observado es [cuaderno, acción 8]:

`nombre.apellido@ubisoft.com`

También se identificó alguna excepción al patrón, sin reproducir direcciones personales [cuaderno, acción 8].

Algunas direcciones aparecían con estado de verificación pendiente, por lo que no se puede asegurar que todas estén activas o verificadas [cuaderno, acción 8].

La información recopilada permite identificar parte de la estructura organizativa de Ubisoft y algunos puestos relevantes en las áreas de dirección, tecnología, informática y legal.

## 5. Puntos de interés

A partir de los resultados del reconocimiento pasivo, se seleccionan tres elementos que sería interesante estudiar primero en una futura fase activa, siempre que estén incluidos en el alcance y se respeten las condiciones del programa de divulgación responsable.

### 1. Subdominios relacionados con infraestructura y monitorización

Ejemplos:

- `grafana.drp.avtr.ubisoft.com`
- `influxdb.live.avtr.ubisoft.com`
- `chef-infra-server.ubisoft.com`

**Motivo:** Los nombres sugieren posibles servicios de monitorización, almacenamiento de métricas y gestión de infraestructura [cuaderno, acción 3]. Sería interesante conocer su exposición y comprobar su configuración dentro de los límites autorizados.

### 2. Servicios asociados a Ubisoft Connect

Ejemplos:

- `dev.ubisoftconnect.com`
- `cert2.ubisoftconnect.com`
- `qr.ubisoftconnect.com`

**Motivo:** Estos subdominios parecen estar relacionados con entornos de desarrollo, certificación y servicios de Ubisoft Connect [cuaderno, acción 3]. Su análisis permitiría comprender mejor la superficie tecnológica de esta plataforma y diferenciar los entornos públicos de los que pudieran estar destinados a pruebas.

### 3. Directorios públicos de `patches.ubi.com`

**Motivo:** Durante las búsquedas de Google se encontraron directorios indexados públicamente que contienen archivos de actualización y ejecutables de distintos videojuegos [cuaderno, acción 7]. Sería interesante estudiar qué información exponen, cómo está organizada y si existen datos publicados accidentalmente, sin descargar ni modificar información fuera de lo permitido.
