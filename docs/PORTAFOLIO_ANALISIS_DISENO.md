# Portafolio de Análisis y Diseño de Software

**Asignatura:** Ingeniería de Software  
**Unidad:** 2 - Análisis y Diseño de Sistemas  
**Proyecto:** Sistema de Gestión y Seguimiento de Estadías Profesionales  
**Integrantes:** Arely Rodríguez Vargas y Eder Nieto Aguilar  

---

## 1. Introducción

El presente portafolio reúne los documentos de análisis y diseño elaborados durante la Unidad 2 de Ingeniería de Software.

El proyecto consiste en desarrollar una plataforma web que permita a los estudiantes universitarios registrar sus estadías profesionales, llevar una bitácora de actividades y entregar evidencias de sus avances.

También permitirá que los asesores académicos revisen las entregas, realicen observaciones y aprueben los documentos.

El objetivo de este portafolio es comprobar que los requisitos del sistema estén relacionados con los diagramas UML, la arquitectura y el diseño de la base de datos.

| Semana | Documento | Contenido |
|---|---|---|
| 6 | [FACTIBILIDAD_PLANIFICACION.md](FACTIBILIDAD_PLANIFICACION.md) | Factibilidad técnica, económica y operativa, Gantt y matriz RACI. |
| 7 | [SRS_IEEE830.md](SRS_IEEE830.md) | Requisitos funcionales, no funcionales, casos de uso y secuencia. |
| 8 | [MODELADO_UML.md](MODELADO_UML.md) | Diagramas de clases, componentes y arquitectura. |
| 8 | [DISEÑO_BD.md](DISEÑO_BD.md) | Tablas, campos y relaciones de la base de datos. |
| 9 | [ARQUITECTURA_DISENO.md](ARQUITECTURA_DISENO.md) | Patrón MVC, arquitectura de tres capas y endpoints HTTP propuestos. |
| 10 | [PORTAFOLIO_ANALISIS_DISENO.md](PORTAFOLIO_ANALISIS_DISENO.md) | Integración y revisión de consistencia entre documentos. |

## 3. Trazabilidad de Requisitos Funcionales

La trazabilidad permite identificar cómo se relaciona cada requisito funcional con las historias de usuario, los casos de uso, las clases y las tablas de la base de datos.

### Matriz de Trazabilidad

| Requisito | Historia | Caso de Uso | Clases Relacionadas | Tabla SQL |
|---|---|---|---|---|
| RF-01: Registro de usuarios | HU-01 | CU-01 | Usuario | usuarios |
| RF-02: Inicio de sesión | HU-02 | CU-02 | Usuario | usuarios |
| RF-03: Registro de estadías | HU-03 | CU-03 | Usuario, Estadia | estadias, usuarios |
| RF-04: Registro de actividades | HU-04 | CU-04 | Estadia, Actividad | actividades, estadias |
| RF-05: Entrega de evidencias | HU-05 | CU-05 | Evidencia, Estadia | evidencias, estadias |
| RF-06: Revisión de entregas | HU-06 | CU-06 | Revision, Evidencia, Usuario | revisiones, evidencias, usuarios |

Esta matriz permite comprobar que los seis requisitos funcionales cuentan con un caso de uso y están relacionados con las entidades que utilizará el sistema.

## 4. Relación entre UML y Base de Datos

El modelo de clases incluye cinco entidades principales que también aparecen en el diseño relacional.

| Clase UML | Tabla SQLite | Relación |
|---|---|---|
| Usuario | usuarios | Contiene estudiantes y asesores. |
| Estadia | estadias | Relaciona al estudiante, asesor y proyecto. |
| Actividad | actividades | Registra las actividades de cada estadía. |
| Evidencia | evidencias | Guarda información de los documentos entregados. |
| Revision | revisiones | Registra observaciones y decisiones del asesor. |

Las tablas utilizan llaves primarias y foráneas para mantener las relaciones entre los datos.

El archivo `database/schema.sql` contiene la implementación de estas estructuras.

### Verificación de Atributos y Tipos de Datos

Se realizó una comparación entre las clases definidas en el diagrama UML y las tablas del archivo `database/schema.sql`.

| Clase UML | Atributos Principales | Tabla SQL | Resultado |
|---|---|---|---|
| Usuario | id, nombre, correo, password_hash, rol | usuarios | Coinciden |
| Estadia | id, estudiante_id, asesor_id, empresa, nombre_proyecto, fecha_inicio, fecha_fin, estado | estadias | Coinciden |
| Actividad | id, estadia_id, fecha, descripcion | actividades | Coinciden |
| Evidencia | id, estadia_id, nombre_archivo, ruta_archivo, fecha_entrega, estado | evidencias | Coinciden |
| Revision | id, evidencia_id, asesor_id, observaciones, resultado, fecha_revision | revisiones | Coinciden |

### Correspondencia de Tipos de Datos

Los tipos de datos del modelo UML tienen las siguientes equivalencias en SQLite:

| Tipo UML | Tipo SQLite | Uso |
|---|---|---|
| int | INTEGER | Identificadores |
| string | TEXT | Nombres, correos y descripciones |
| date | TEXT | Fechas en formato AAAA-MM-DD |

SQLite permite almacenar las fechas como texto, por lo que se utilizará un formato consistente para facilitar las consultas.

### Verificación de Relaciones

Las relaciones principales del sistema son:

1. Un estudiante puede registrar varias estadías.
2. Un asesor puede supervisar varias estadías.
3. Una estadía puede contener varias actividades.
4. Una estadía puede tener varias evidencias.
5. Una evidencia puede recibir varias revisiones.
6. Un asesor puede realizar varias revisiones.

Estas relaciones están representadas mediante multiplicidades en el diagrama de clases y llaves foráneas en el esquema SQL.

### Resultado de la Verificación

La comparación documental muestra que las cinco clases persistentes contienen los mismos campos principales que sus tablas correspondientes.

Se identificó una diferencia de representación en los campos de fecha, ya que UML utiliza el tipo `date` y SQLite utiliza `TEXT`.

También será necesario validar durante la implementación que los usuarios relacionados con una estadía tengan el rol correcto y que las fechas se almacenen en el formato establecido.

Por lo tanto, se considera que existe consistencia estructural entre el diagrama de clases y el esquema SQL, con las consideraciones mencionadas.

## 5. Consistencia de la Arquitectura

Se propone utilizar una arquitectura de tres capas organizada mediante los principios del patrón Modelo-Vista-Controlador (MVC).

### Capa de Presentación

Permitirá que estudiantes y asesores interactúen con el sistema mediante páginas HTML y CSS.

### Capa de Lógica de Negocio

Utilizará Python y Flask para procesar solicitudes, validar información y aplicar las reglas del sistema.

### Capa de Datos

Utilizará SQLite para almacenar usuarios, estadías, actividades, evidencias y revisiones.

Los documentos subidos por los estudiantes se almacenarán en una ubicación protegida, mientras que sus datos de referencia se guardarán en la base de datos.

### Relación entre Requisitos, Controladores y Endpoints HTTP

Para mantener la consistencia entre el análisis y el diseño, se establece la relación entre los requisitos funcionales, las operaciones propuestas y los endpoints HTTP.

| Requisito | Operación del Controlador | Método HTTP | Endpoint |
|---|---|---|---|
| RF-01: Registro de usuarios | registrar_usuario() | POST | /registro |
| RF-02: Inicio de sesión | iniciar_sesion() | POST | /login |
| RF-03: Registro de estadías | registrar_estadia() | POST | /estadias |
| RF-04: Registro de actividades | registrar_actividad() | POST | /actividades |
| RF-05: Entrega de evidencias | subir_evidencia() | POST | /evidencias |
| RF-06: Revisión de entregas | revisar_evidencia() | PUT | /evidencias/{id}/revision |

### Justificación

Cada endpoint corresponde a una función identificada durante el análisis de requisitos.

Se utilizará el método POST para registrar información nueva, mientras que PUT permitirá actualizar el resultado de una revisión.

Las operaciones serán procesadas mediante controladores desarrollados con Python y Flask.

Estos controladores se comunicarán con la capa de datos para almacenar o consultar información en SQLite.

### Estado de Implementación

Los endpoints y métodos presentados forman parte del diseño propuesto.

Actualmente, la aplicación cuenta con una página principal y un formulario de inicio de sesión.

Todavía falta implementar el registro de usuarios, la autenticación con base de datos, el registro de estadías, las actividades y la gestión de evidencias.

Durante la etapa de desarrollo se comprobará que las rutas implementadas coincidan con esta especificación.

## 6. Requisitos No Funcionales

Se definieron cinco requisitos relacionados con la calidad del software.

| Código | Característica de Calidad | Criterio Propuesto |
|---|---|---|
| RNF-01 | Rendimiento | Respuesta máxima de 2 segundos con 20 usuarios concurrentes en pruebas. |
| RNF-02 | Seguridad | Contraseñas protegidas mediante hash y permisos según el rol. |
| RNF-03 | Mantenibilidad | Cumplimiento de PEP 8 y objetivo de 80% de cobertura de pruebas unitarias. |
| RNF-04 | Usabilidad | Al menos 4 de cada 5 usuarios de prueba completarán las tareas principales sin ayuda. |
| RNF-05 | Confiabilidad | Validación de datos y prevención de pérdida de información ante errores. |

Estas condiciones representan objetivos que deberán comprobarse durante las etapas de desarrollo y pruebas.

## 7. Auditoría de Consistencia entre Modelos

Se realizó una revisión documental preliminar para identificar la correspondencia entre los diferentes modelos del sistema.

| Criterio de Auditoría | Resultado | Observaciones |
|---|---|---|
| Los seis requisitos funcionales tienen un caso de uso identificado. | Cumple | RF-01 a RF-06 corresponden con CU-01 a CU-06. |
| Los seis requisitos funcionales cuentan con diagramas de secuencia. | Cumple | Se documentaron los procesos principales de cada requisito. |
| Las cinco clases persistentes tienen una tabla SQL correspondiente. | Cumple | Usuario, Estadia, Actividad, Evidencia y Revision. |
| El esquema SQL define llaves primarias y foráneas. | Cumple | Las cinco tablas incluyen llaves primarias y las relaciones correspondientes. |
| Los RNF incluyen criterios de calidad. | Cumple parcialmente | Se deben precisar algunas métricas de confiabilidad y seguridad. |
| Los atributos del diagrama de clases coinciden con las tablas SQL. | Cumple con observaciones | Los campos coinciden; las fechas se representan como date en UML y TEXT en SQLite. |
| Los métodos de control corresponden a los endpoints HTTP. | Cumple a nivel de diseño | Se documentó la relación entre los seis RF, operaciones propuestas y endpoints. La implementación sigue pendiente. |
| Los documentos están organizados en la carpeta docs. | Cumple | Los documentos principales de la Unidad 2 están organizados. |
| Se realizó una revisión con otro equipo. | Pendiente | Se solicitarán observaciones durante la auditoría cruzada. |

### Observaciones

Durante la revisión de consistencia se comprobó que los seis requisitos funcionales cuentan con casos de uso y diagramas de secuencia relacionados.

También se identificó que las cinco clases principales del sistema tienen una tabla correspondiente en SQLite.

Sin embargo, todavía es necesario realizar las siguientes actividades:

1. Comparar detalladamente los atributos del diagrama de clases con los campos de las tablas SQL.
2. Verificar que los métodos de control correspondan con los endpoints HTTP propuestos.
3. Fortalecer las métricas de los requisitos no funcionales.
4. Solicitar una revisión externa a otro equipo para identificar posibles errores.

Estas actividades permitirán mejorar la calidad y consistencia del diseño antes de continuar con el desarrollo del sistema.

## 8. Conclusión

La elaboración del portafolio permitió reunir los documentos de análisis y diseño del Sistema de Gestión y Seguimiento de Estadías Profesionales.

Mediante los requisitos, diagramas UML, arquitectura y esquema de base de datos se estableció una estructura inicial para desarrollar el software.

La matriz de trazabilidad facilita identificar las funciones del sistema y los elementos relacionados con su implementación.

Finalmente, la auditoría preliminar permitió detectar aspectos que necesitan mejoras, demostrando la importancia de revisar el diseño antes y durante la programación.