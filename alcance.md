# Alcance del proyecto - Ubisoft

## 1. Enlace al programa y fecha de consulta.

- **Organización:** Ubisoft.
- **Programa:** Ubisoft Responsible Disclosure Program.
- **Plataforma:** Intigriti.
- **Tipo:** Vulnerability Disclosure Program (VDP) público.
- **URL:** https://app.intigriti.com/programs/ubisoft/ubisoftvdp/detail
- **Fecha de consulta:** 02/11/2026.
- **Recompensas:** No ofrece recompensas económicas.

## 2. Descripción del alcance

El programa permite comunicar vulnerabilidades de seguridad relacionadas con servicios de Ubisoft expuestos a Internet, aplicaciones oficiales y videojuegos incluidos expresamente en el programa.

### Activos dentro del alcance

**Aplicaciones web y servicios corporativos:**

- Aplicaciones web y API públicas propiedad y operadas por Ubisoft.
- Dominios de ejemplo indicados en el programa:
  - `*.ubisoft.com`
  - `*.ubi.com`
  - `*.ubisoftconnect.com`
- La política describe como dentro del alcance las aplicaciones web y API públicas propiedad y operadas por Ubisoft, y presenta esos comodines como ejemplos. Por ello, los dominios raíz `ubisoft.com`, `ubi.com` y `ubisoftconnect.com` se incluyen por separado en `scope.txt` como sitios públicos oficiales de Ubisoft; no se deduce su inclusión de la sintaxis de los comodines.
- Aplicaciones oficiales de escritorio, como Ubisoft Connect.
- Aplicaciones móviles oficiales destinadas a servicios corporativos, gestión de cuentas o funcionalidades complementarias.
- Infraestructura corporativa y servicios online propiedad y operados por Ubisoft.

**Videojuegos incluidos:**

Entre los títulos indicados en el programa se encuentran Rainbow Six Siege, The Division 2, For Honor, Skull & Bones, The Crew: Motorfest, Just Dance, Watch Dogs Legion, Brawlhalla y Assassin's Creed Shadows, entre otros.

### Activos fuera del alcance

- `forums.ubisoft.com`
- `ivalua.ubisoft.com`
- `suppliers-ivalua.ubisoft.com`
- The Settlers Online.
- Dominios que no pertenezcan a Ubisoft o que no estén incluidos en el alcance indicado.
- Servicios de terceros que Ubisoft no controle.

## 3. Reglas

- El programa exige respetar el alcance y las condiciones de Intigriti.
- Las herramientas automatizadas tienen un límite máximo de 2 solicitudes por segundo.
- Las solicitudes de pruebas del programa requieren la cabecera `X-Intigriti-Username`.
- Se deben utilizar cuentas propias cuando las pruebas autorizadas requieran una cuenta.
- Está prohibido acceder a cuentas de otros usuarios o a información confidencial.
- No se permite afectar a otros jugadores ni perjudicar la disponibilidad de los servicios.
- No están permitidos los ataques de ingeniería social, phishing ni las intrusiones físicas.
- No se permite realizar pruebas destructivas, DoS/DDoS o fuerza bruta a gran escala.
- La información personal que se encuentre accidentalmente está fuera del alcance. Se debe detener la investigación y no almacenarla ni copiarla.
- No se pueden divulgar públicamente los detalles de vulnerabilidades encontradas sin autorización expresa de Ubisoft.
- El programa dispone de protección de puerto seguro (Safe Harbour) para investigadores que respeten sus condiciones.
