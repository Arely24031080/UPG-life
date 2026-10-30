
# Reporte Técnico de Selección y Justificación Metodológica

**Asignatura:** Ingeniería de Software  
**Unidad 1:** Reporte de Selección y Justificación de la Metodología  
**Proyecto Final:** Sistema de Gestión y Seguimiento de Estadías Profesionales  
**Equipo de Desarrollo:** Equipo UPG-life  
**Fecha:** 22/10/2026  

---

## 1. Caracterización del Sistema y Entorno de Proyecto

**Ámbito de Dominio:**

Gestión académica, desarrollo de software y administración de información.

**Problema Principal a Resolver:**

Actualmente, los estudiantes pueden registrar sus estadías profesionales y al maestro asignado, pero no cuentan con un sistema completo para dar seguimiento a sus actividades y avances. Esto puede dificultar la organización de reportes, evidencias y revisiones por parte de los asesores.

Por ello, se propone desarrollar una plataforma web que permita a los estudiantes registrar sus actividades, subir evidencias y consultar el estado de sus entregas. Los asesores podrán revisar los avances, realizar observaciones y aprobar los trabajos.

**Complejidad Técnica y Criticidad:**

El proyecto tiene una complejidad media, ya que requiere desarrollar una interfaz web, una base de datos y diferentes funciones para estudiantes y asesores.

El sistema deberá permitir el almacenamiento de documentos, el seguimiento de actividades y la revisión de entregas. También será importante proteger la información personal de los estudiantes, evitar pérdidas de datos y garantizar que cada usuario tenga acceso únicamente a las funciones que le corresponden.

**Perfil de Integrantes y Cliente:**

El proyecto será desarrollado por estudiantes de Ingeniería en Datos e Inteligencia Artificial, utilizando conocimientos de programación, bases de datos y desarrollo web.

El equipo se encargará del diseño, programación y pruebas del sistema. Para orientar el desarrollo, se considerarán las necesidades de los estudiantes y asesores académicos, quienes podrán proporcionar retroalimentación sobre las funciones propuestas.


## 2. Evaluación Multicriterio de Alternativas Metodológicas

Para seleccionar la metodología más adecuada para nuestro sistema de gestión y seguimiento de estadías profesionales, se compararon diferentes enfoques de desarrollo de software.

| Criterio de Evaluación | Enfoque Clásico (Cascada/Espiral) | Enfoque Ágil (Scrum/XP) | Enfoque Híbrido Propuesto |
|---|---|---|---|
| Gestión de Cambios | Los cambios pueden ser difíciles de realizar cuando ya se terminaron algunas etapas. | Permite realizar modificaciones durante el desarrollo. | Se establece una planificación inicial, pero se permiten cambios en cada Sprint. |
| Documentación Exigida | Requiere documentación detallada durante las etapas del proyecto. | Utiliza documentación sencilla y necesaria, como historias de usuario. | Se documentan los requisitos principales y se actualizan durante el desarrollo. |
| Participación del Cliente | El cliente participa principalmente en etapas específicas. | El cliente puede revisar los avances constantemente. | Los estudiantes y asesores podrán proporcionar comentarios al finalizar cada Sprint. |
| Velocidad de Entrega | Generalmente se entrega el sistema completo al finalizar el desarrollo. | Permite entregar pequeñas funcionalidades en periodos cortos. | Se desarrollarán primero las funciones principales y después se agregarán mejoras. |

Después de analizar las alternativas, consideramos que un enfoque híbrido basado en Scrum es adecuado para nuestro proyecto, ya que permite organizar el trabajo, mantener la documentación necesaria y realizar mejoras durante el desarrollo.


## 3. Justificación Fundada de la Metodología Seleccionada

**Metodología Seleccionada:**

Enfoque híbrido basado en Scrum.

**Argumentación Técnica Fundamentada:**

Se seleccionó un enfoque híbrido basado en Scrum porque permite organizar el desarrollo del sistema de gestión y seguimiento de estadías profesionales en etapas cortas, facilitando la distribución de actividades entre los integrantes del equipo.

De acuerdo con los principios de ingeniería de software explicados por Sommerville (2011, capítulo 2), la elección del proceso de desarrollo debe considerar las características y necesidades de cada proyecto.

En nuestro caso, se necesita desarrollar diferentes funciones, como el registro de actividades, la entrega de evidencias, la revisión de documentos y el seguimiento de avances.

Esta metodología nos permitirá comenzar con una planificación de los requisitos principales y después desarrollar las funciones mediante Sprints. Al finalizar cada Sprint, podremos revisar los resultados, identificar errores y realizar las mejoras necesarias.

Además, ayudará a aprovechar mejor el tiempo, reducir el trabajo repetido y mantener la calidad del sistema mediante pruebas y revisiones.

Por estas razones, consideramos que el enfoque híbrido basado en Scrum es adecuado para nuestro proyecto, ya que combina la organización de la documentación con la flexibilidad para realizar cambios durante el desarrollo.

**Referencia:**

Sommerville, I. (2011). Ingeniería de software (9.ª ed.). Pearson. Capítulo 2.


## 4. Definición del Proceso Adaptado y Artefactos

**Fases o Ciclos del Proceso:**

El desarrollo del sistema se organizará mediante una etapa inicial de planificación y tres Sprints de dos semanas cada uno.

- **Planificación inicial:** Identificar los requisitos del sistema, definir las funciones principales y organizar las actividades del equipo.
- **Sprint 1:** Desarrollar el registro e inicio de sesión de estudiantes y asesores, así como el registro de estadías profesionales.
- **Sprint 2:** Implementar el registro de actividades y la carga de reportes y evidencias.
- **Sprint 3:** Desarrollar la revisión de entregas, las observaciones de los asesores y la visualización del avance de cada estudiante.

Al finalizar cada Sprint, se revisarán los resultados y se realizarán pruebas para identificar posibles errores.

**Artefactos Obligatorios a Generar:**

Durante el desarrollo se elaborarán los siguientes documentos y elementos:

- Documento de requisitos del sistema (SRS, tomando como referencia IEEE 830).
- Diagramas UML para representar las funciones y estructura del sistema.
- Historias de usuario y Product Backlog.
- Planificación de Sprints.
- Código fuente del sistema.
- Pruebas de funcionamiento.
- Manual de usuario.

**Matriz de Responsabilidades del Equipo:**

| Rol | Responsabilidad |
|---|---|
| Product Owner | Definir las necesidades y prioridades del sistema. |
| Scrum Master | Organizar las actividades y dar seguimiento a los Sprints. |
| Equipo de Desarrollo | Diseñar, programar e integrar las funciones del sistema. |
| QA (Calidad) | Realizar pruebas y verificar que las funciones trabajen correctamente. |

Los roles serán distribuidos entre los integrantes del equipo. Una persona podrá participar en más de una responsabilidad cuando sea necesario.


## 5. Compromiso de Calidad y Gobernanza de Código

**Alineación con PARADIGMA.md y CALIDAD.md:**

Para el desarrollo del sistema de gestión y seguimiento de estadías profesionales, se tomarán como referencia los acuerdos establecidos en los archivos PARADIGMA.md y CALIDAD.md del repositorio.

Se utilizarán herramientas y buenas prácticas de programación para mantener un código organizado, comprensible y fácil de modificar.

También se considerarán los atributos de calidad de la norma ISO/IEC 25010, principalmente:

- **Mantenibilidad:** El código estará organizado en módulos para facilitar futuras modificaciones y correcciones.
- **Confiabilidad:** Se realizarán pruebas para comprobar que las funciones del sistema trabajen correctamente.
- **Seguridad:** Se protegerá la información de estudiantes y asesores mediante el control de acceso según el tipo de usuario.
- **Usabilidad:** Se buscará que la plataforma sea sencilla de utilizar y que sus funciones sean claras.

Además, se utilizarán herramientas de revisión de código (linters) para identificar problemas de estilo y mantener una estructura consistente.

**Mecanismos de Control de Cambios:**

Para organizar los cambios del proyecto, se utilizará Git y GitHub.

Cada nueva funcionalidad se desarrollará en una rama independiente, evitando modificar directamente la rama principal (main).

Los cambios se guardarán mediante commits con mensajes descriptivos y posteriormente se enviarán a GitHub.

Antes de integrar los cambios a la rama principal, se creará un Pull Request para que otro integrante del equipo revise el código y la documentación.

Una vez aprobados los cambios, se realizará el Merge a main.

Este procedimiento permitirá mantener un historial de modificaciones, facilitar el trabajo en equipo y reducir los errores durante el desarrollo.
