

He completado el reconocimiento pasivo de `ubisoft.com`. Aquí está el informe:

---

# Informe de Reconocimiento Pasivo — ubisoft.com

## 1. Registro del Dominio (WHOIS)

| Dato | Valor | Fuente |
|------|-------|--------|
| Dominio | UBISOFT.COM | `whois_dominio` |
| Fecha de registro | 1995-04-27 | `whois_dominio` |
| Fecha de caducidad | 2033-04-28 | `whois_dominio` |
| Última modificación | 2026-10-13 | `whois_dominio` |
| Registrador | Entidad 81 (gandi.net) | `whois_dominio` / `netcraft_info` |
| Estado | client transfer prohibited | `whois_dominio` |
| Nameservers | NIC7-12.UBISOFT.COM (6 servidores) | `whois_dominio` |

## 2. Registros DNS

### A (IPv4)
- `52.222.177.30`
- `52.222.177.123`
- `52.222.177.121`
- `52.222.177.122`
- **Fuente:** `dns_registros`

### AAAA (IPv6)
- Sin registros AAAA.
- **Fuente:** `dns_registros`

### CNAME
- Sin registros CNAME.
- **Fuente:** `dns_registros`

### MX (Correo)
- `10 ubisoftaad.mail.protection.outlook.com.`
- **Fuente:** `dns_registros`

### NS (Nameservers)
- `nic10.ubisoft.com.`
- `nic8.ubisoft.com.`
- `nic12.ubisoft.com.`
- `nic11.ubisoft.com.`
- `nic9.ubisoft.com.`
- `nic7.ubisoft.com.`
- **Fuente:** `dns_registros`

### SOA
- Primary NS: `nic7.ubisoft.com.`
- Email: `hostmaster.ubisoft.com.`
- Serial: `2023127420`
- Refresh: `21600` | Retry: `3600` | Expire: `604800` | Minimum TTL: `600`
- **Fuente:** `dns_registros`

### TXT (Verificaciones y SPF)
- **SPF:** `v=spf1 redirect=_spf.ubisoft.com`
- **Verificaciones de terceros:** Google, Apple, Yahoo, Facebook, Microsoft, Atlassian, Anthropic, Yandex, Miro, Docker, MongoDB, Docusign, Bugcrowd, Parsec, Meltwater, Miro, Workplace, Tracción, OneTrust, SFCC, MindManager y otras.
- **Fuente:** `dns_registros`

## 3. Subdominios (crt.sh)

- **Total:** 750 subdominios dentro del alcance.
- **Filtrados por estar fuera:** 5 (corresponden a dominios excluidos como `forums.ubisoft.com`, `ivalua.ubisoft.com`, etc.).
- **Ejemplos relevantes:** `account.ubisoft.com`, `cdn.ubisoft.com`, `cloud.ubisoft.com`, `art.ubisoft.com`, `club.ubisoft.com`, `creators.ubisoft.com`, `api.splunk.sink.ubisoft.com`, `authy.upn-poc.ubisoft.com`, `autodiscover.ubisoft.com`, `admin.s2s.shipyard-prompoc.raftman-sandbox-metrics.ubisoft.com`, etc.
- **Fuente:** `subdominios_crtsh`

## 4. Cabeceras HTTP de Seguridad

| Cabecera | Estado | Valor | Fuente |
|----------|--------|-------|--------|
| Strict-Transport-Security | ❌ FALTA | — | `cabeceras_http` |
| Content-Security-Policy | ✅ OK | `frame-ancestors 'self';` | `cabeceras_http` |
| X-Frame-Options | ❌ FALTA | — | `cabeceras_http` |
| X-Content-Type-Options | ❌ FALTA | — | `cabeceras_http` |
| Referrer-Policy | ❌ FALTA | — | `cabeceras_http` |

- **Código HTTP:** 200
- **Fuente:** `cabeceras_http`

## 5. robots.txt y security.txt

### robots.txt
```
User-Agent: *
Disallow: /entertainment/parks-experiences/escape-games/downloads
Disallow: /search?gss-q=*
Disallow: /legal/documents/PrivacyNoticeSmartrecruiters/
Disallow: /legal/documents/PrivacyNoticeMicrosoftTeams/
Disallow: /legal/documents/PrivacyNoticeRecruitment/

Sitemap: https://www.ubisoft.com/sitemap.xml
```
- **Fuente:** `robots_security`

### security.txt
- **No encontrado (HTTP 404)**
- **Fuente:** `robots_security`

## 6. Informe Netcraft

| Dato | Valor | Fuente |
|------|-------|--------|
| Site rank | 408084 | `netcraft_info` |
| Primera vez visto | Diciembre 2014 | `netcraft_info` |
| Propietario del netblock | Amazon.com, Inc. | `netcraft_info` |
| Empresa de hosting | Amazon | `netcraft_info` |
| País de hosting | US | `netcraft_info` |
| IPv4 | 52.222.177.121 | `netcraft_info` |
| IPv4 AS | AS16509 | `netcraft_info` |
| IPv6 | No presente | `netcraft_info` |
| Reverse DNS | server-52-222-177-121.lhr95.r.cloudfront.net | `netcraft_info` |
| Registrador | gandi.net | `netcraft_info` |
| Nameserver | nic7.ubisoft.com | `netcraft_info` |
| Organización | Ubisoft Entertainment, France | `netcraft_info` |
| DNS admin | [email protected] | `netcraft_info` |
| DNS Security Extensions (DNSSEC) | Habilitado | `netcraft_info` |

---

### Observaciones clave

1. **Hosting:** El tráfico web de `ubisoft.com` está alojado en **Amazon CloudFront** (AS16509), con reverse DNS en `lhr95.r.cloudfront.net` (Londres).
2. **Correo:** El servicio de correo está gestionado por **Microsoft 365** (`ubisoftaad.mail.protection.outlook.com`).
3. **Seguridad HTTP:** Faltan cabeceras importantes como **HSTS**, **X-Frame-Options**, **X-Content-Type-Options** y **Referrer-Policy**. Solo está presente CSP con una directiva `frame-ancestors 'self'`.
4. **DNSSEC:** Habilitado ✅ según Netcraft.
5. **Subdominios:** 750 activos identificados vía certificados, indicando una infraestructura extensa con entornos de producción, desarrollo, staging, y servicios internos (Splunk, Shipyard, Vault, Upn-Poc, R6Q, etc.).
6. **security.txt:** No implementado (404), lo que dificulta el contacto directo para reportes de seguridad.