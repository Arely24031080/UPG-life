#MATRIZ DE ATRIBUTOS DE CALIDAD Y ESTANDARES ( SOMMERVILLE CAP. 24)

### 1. Mantenibilidad (Maintainability)
- **Metrica Objetivo:** Maximo 15 lineas por funcion; complejidad ciclomatica <5.
- **Estandar de Codificacion:** Cumplimiento del estandar PEP 8 mediante Flake8 con 0 advetencias de sintaxis.
- **Nomenclatura:** Identificadores significativamente en español o ingles (variables `snake_case`, clases `PascalCase`).

### 2. Cinfiabilidad y Seguridad (Dependability & Security)
- **Validación de Entradas:** Manejo explícito de excepciones (bloques `try-except`) evitando capturas genéricas.
- **Control de Datos:** Exclusión de credenciales, contraseñas o tokens en el código fuente mediante `.gitignore`.

### 3. Eficiencia (Efficiency)
- **Uso de Memoria:** Liberación explícita de recursos y uso de estructuras de datos adecuadas (listas vs diccionarios).

### 4. Aceptabilidad (Acceptability)
- **Documentación de Funciones:** Todo método público debe incluir un docstring explicativo breve sobre parámetros y retornos.