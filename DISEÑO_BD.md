
# Diseño de la Base de Datos

**Proyecto:** Sistema de Gestión y Seguimiento de Estadías Profesionales

**Asignatura:** Ingeniería de Software

**Unidad:** 2 - Análisis y Diseño de Sistemas de Software

## 1. Descripción General

La base de datos permitirá almacenar y organizar la información de los estudiantes, asesores académicos, estadías profesionales, actividades, evidencias y revisiones.

Se utilizará SQLite, ya que es una base de datos relacional gratuita, sencilla de implementar y adecuada para el desarrollo inicial del sistema.

La información se organizará en cinco tablas relacionadas mediante llaves primarias y foráneas para evitar registros inconsistentes.

## 2. Tablas de la Base de Datos

### Tabla 1. Usuarios

Almacenará los datos de estudiantes y asesores académicos.

| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Identificador único del usuario |
| nombre | TEXT | Nombre completo |
| correo | TEXT | Correo electrónico único |
| password_hash | TEXT | Contraseña protegida mediante hash |
| rol | TEXT | Estudiante o asesor |

### Tabla 2. Estadías

Almacenará la información de las estadías profesionales.

| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Identificador de la estadía |
| estudiante_id | INTEGER | Estudiante registrado |
| asesor_id | INTEGER | Asesor académico asignado |
| empresa | TEXT | Nombre de la empresa |
| nombre_proyecto | TEXT | Nombre del proyecto |
| fecha_inicio | TEXT | Fecha de inicio |
| fecha_fin | TEXT | Fecha de finalización |
| estado | TEXT | Estado de la estadía |

### Tabla 3. Actividades

Guardará las actividades realizadas durante las estadías.

| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Identificador de la actividad |
| estadia_id | INTEGER | Estadía relacionada |
| fecha | TEXT | Fecha de la actividad |
| descripcion | TEXT | Trabajo realizado |

### Tabla 4. Evidencias

Almacenará la información de los documentos entregados.

| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Identificador de la evidencia |
| estadia_id | INTEGER | Estadía relacionada |
| nombre_archivo | TEXT | Nombre del documento |
| ruta_archivo | TEXT | Ubicación del archivo |
| fecha_entrega | TEXT | Fecha de entrega |
| estado | TEXT | Pendiente, aprobada o corrección requerida |

### Tabla 5. Revisiones

Guardará las observaciones y decisiones de los asesores.

| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Identificador de la revisión |
| evidencia_id | INTEGER | Evidencia revisada |
| asesor_id | INTEGER | Asesor responsable |
| observaciones | TEXT | Comentarios del asesor |
| resultado | TEXT | Aprobada o corrección requerida |
| fecha_revision | TEXT | Fecha de revisión |

## 3. Relaciones entre Tablas

- Un estudiante puede tener varias estadías profesionales.
- Un asesor puede supervisar varias estadías.
- Cada estadía pertenece a un estudiante y tiene un asesor asignado.
- Una estadía puede contener varias actividades.
- Una estadía puede tener varias evidencias.
- Una evidencia puede recibir varias revisiones.
- Un asesor puede realizar varias revisiones.

Las relaciones se establecerán mediante llaves foráneas para mantener la integridad de los datos.

## 4. Integridad de la Información

Para evitar problemas en el almacenamiento de información se aplicarán las siguientes reglas:

- Cada tabla tendrá una llave primaria.
- Los correos electrónicos de los usuarios no podrán repetirse.
- Los campos obligatorios no podrán quedar vacíos.
- Las llaves foráneas permitirán relacionar correctamente las tablas.
- Se validarán los roles de los usuarios y los estados de las entregas.
- Se evitará eliminar información relacionada con evidencias y revisiones sin autorización.

El diseño permitirá mantener la información organizada y facilitar futuras modificaciones del sistema.
