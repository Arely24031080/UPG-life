
# MATRIZ DE ATRIBUTOS DE CALIDAD Y ESTÁNDARES
**Referencia:** Sommerville, Capítulo 24 e ISO/IEC 25010.

**Proyecto:** Sistema de Gestión y Seguimiento de Estadías Profesionales.

## 1. Mantenibilidad (Maintainability)

- **Métrica Objetivo:** Procurar un máximo de 15 líneas por función y una complejidad ciclomática menor a 5.
- **Estándar de Codificación:** Cumplimiento del estándar PEP 8 mediante Flake8, sin errores de sintaxis ni estilo reportados.
- **Nomenclatura:** Utilizar nombres claros en español o inglés, variables en `snake_case` y clases en `PascalCase`.
- **Organización:** Dividir el sistema en módulos para facilitar las modificaciones y correcciones.

## 2. Confiabilidad y Seguridad (Dependability & Security)

- **Validación de Entradas:** Verificar que los campos obligatorios estén completos y utilizar bloques `try-except` para manejar errores.
- **Control de Acceso:** Los estudiantes podrán consultar sus propias actividades y evidencias, mientras que los asesores podrán revisar las entregas de sus estudiantes asignados.
- **Protección de Datos:** Evitar almacenar contraseñas en texto plano y no publicar credenciales ni información sensible en GitHub.
- **Control de Archivos:** Validar el tipo y tamaño de los documentos que los estudiantes suban al sistema.
- **Pruebas:** Comprobar que el registro, inicio de sesión, carga de evidencias y revisión de entregas funcionen correctamente.

## 3. Eficiencia (Efficiency)

- **Uso de Memoria:** Utilizar estructuras de datos adecuadas y liberar los recursos que ya no se necesitan.
- **Consultas:** Organizar las consultas a la base de datos para recuperar la información de manera eficiente.
- **Almacenamiento:** Establecer límites para los archivos y evitar guardar documentos duplicados innecesariamente.

## 4. Aceptabilidad y Usabilidad (Acceptability & Usability)

- **Interfaz:** Diseñar pantallas sencillas y comprensibles para estudiantes y asesores.
- **Mensajes:** Mostrar confirmaciones y errores claros al registrar información o subir documentos.
- **Documentación de Funciones:** Los métodos públicos deberán incluir un docstring breve que explique su funcionamiento, parámetros y resultados.
- **Pruebas de Usuario:** Verificar que las funciones principales sean fáciles de utilizar.

## 5. Control de Calidad del Desarrollo

- Revisar el código mediante Pull Requests antes de integrarlo a `main`.
- Utilizar Flake8 para detectar problemas de estilo.
- Realizar pruebas de las funciones desarrolladas en cada Sprint.
- Corregir los errores detectados antes de considerar terminada una historia de usuario.
- Mantener actualizada la documentación del proyecto.
