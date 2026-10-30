
# Inventario de Historias de Usuario - Proyecto Final

**Proyecto:** Sistema de Gestión y Seguimiento de Estadías Profesionales

## HU-01: Registro de usuario

- **ID:** HU-01
- **Nombre:** Registro de usuario
- **Como:** Estudiante universitario.
- **Quiero:** Registrarme en el sistema con mis datos personales y académicos.
- **Para:** Acceder a la plataforma y dar seguimiento a mis estadías profesionales.
- **Estimación (Story Points):** 5
- **Prioridad:** Alta

### Criterios de Aceptación

**Escenario 1: Registro exitoso**
- **Dado que** el estudiante ingresa sus datos correctamente,
- **Cuando** presiona "Registrarse",
- **Entonces** el sistema guarda la información y muestra un mensaje de confirmación.

**Escenario 2: Datos incompletos**
- **Dado que** el estudiante deja campos obligatorios vacíos,
- **Cuando** intenta registrarse,
- **Entonces** el sistema solicita completar la información.

---

## HU-02: Inicio de sesión

- **ID:** HU-02
- **Nombre:** Inicio de sesión
- **Como:** Estudiante o asesor académico.
- **Quiero:** Iniciar sesión con mi correo y contraseña.
- **Para:** Acceder de manera segura a las funciones correspondientes a mi usuario.
- **Estimación (Story Points):** 3
- **Prioridad:** Alta

### Criterios de Aceptación

**Escenario 1: Acceso exitoso**
- **Dado que** el usuario tiene una cuenta registrada,
- **Cuando** ingresa sus datos correctamente,
- **Entonces** el sistema permite el acceso.

**Escenario 2: Datos incorrectos**
- **Dado que** el usuario ingresa datos incorrectos,
- **Cuando** intenta iniciar sesión,
- **Entonces** el sistema muestra un error y no permite el acceso.

---

## HU-03: Registro de estadía profesional

- **ID:** HU-03
- **Nombre:** Registro de estadía profesional
- **Como:** Estudiante universitario.
- **Quiero:** Registrar la empresa, el proyecto y los asesores asignados.
- **Para:** Organizar la información de mi estadía profesional.
- **Estimación (Story Points):** 5
- **Prioridad:** Alta

### Criterios de Aceptación

**Escenario 1: Registro exitoso**
- **Dado que** el estudiante ha iniciado sesión,
- **Cuando** completa los datos de su estadía y presiona "Guardar",
- **Entonces** el sistema almacena la información.

**Escenario 2: Datos incompletos**
- **Dado que** el estudiante deja campos obligatorios vacíos,
- **Cuando** intenta guardar,
- **Entonces** el sistema solicita completar los datos faltantes.

---

## HU-04: Registro de actividades de estadía

- **ID:** HU-04
- **Nombre:** Registro de actividades
- **Como:** Estudiante universitario.
- **Quiero:** Registrar las actividades realizadas durante mis estadías.
- **Para:** Llevar un control de mis avances.
- **Estimación (Story Points):** 5
- **Prioridad:** Alta

### Criterios de Aceptación

**Escenario 1: Registro exitoso**
- **Dado que** el estudiante tiene una estadía registrada,
- **Cuando** ingresa la fecha y descripción de su actividad,
- **Entonces** el sistema guarda la actividad en su historial.

**Escenario 2: Información incompleta**
- **Dado que** el estudiante no completa la descripción,
- **Cuando** intenta guardar,
- **Entonces** el sistema muestra un mensaje de error.

**Escenario 3: Consulta de actividades**
- **Dado que** el estudiante registró actividades,
- **Cuando** consulta su bitácora,
- **Entonces** el sistema muestra las fechas y descripciones.

---

## HU-05: Entrega de reportes y evidencias

- **ID:** HU-05
- **Nombre:** Entrega de reportes y evidencias
- **Como:** Estudiante universitario.
- **Quiero:** Subir reportes y documentos de mis actividades.
- **Para:** Permitir que mi asesor revise el trabajo realizado.
- **Estimación (Story Points):** 5
- **Prioridad:** Alta

### Criterios de Aceptación

**Escenario 1: Entrega exitosa**
- **Dado que** el estudiante tiene una estadía registrada,
- **Cuando** selecciona un archivo válido y presiona "Subir",
- **Entonces** el sistema guarda el documento.

**Escenario 2: Archivo no permitido**
- **Dado que** el estudiante selecciona un archivo no permitido,
- **Cuando** intenta subirlo,
- **Entonces** el sistema muestra un mensaje de error.

**Escenario 3: Consulta de entregas**
- **Dado que** el estudiante ya entregó documentos,
- **Cuando** consulta sus evidencias,
- **Entonces** el sistema muestra los archivos y sus fechas.

---

## HU-06: Revisión y aprobación de evidencias

- **ID:** HU-06
- **Nombre:** Revisión y aprobación de evidencias
- **Como:** Asesor académico.
- **Quiero:** Revisar y evaluar los reportes de mis estudiantes.
- **Para:** Aprobar las entregas o solicitar correcciones.
- **Estimación (Story Points):** 5
- **Prioridad:** Alta

### Criterios de Aceptación

**Escenario 1: Aprobación**
- **Dado que** el estudiante envió un reporte,
- **Cuando** el asesor selecciona "Aprobar",
- **Entonces** el sistema cambia el estado a "Aprobada".

**Escenario 2: Solicitud de corrección**
- **Dado que** el asesor identifica errores,
- **Cuando** escribe observaciones y solicita correcciones,
- **Entonces** el sistema guarda los comentarios y cambia el estado a "Corrección requerida".

**Escenario 3: Consulta de entregas**
- **Dado que** el asesor tiene estudiantes asignados,
- **Cuando** consulta las entregas,
- **Entonces** el sistema muestra los documentos y sus estados.
