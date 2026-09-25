# PARADIGMA DE INGENIERÍA DE SOFTWARE DEL PROYECTO

**Asignatura:** Ingeniería de Software | **Carrera:** Ingeniería en Datos e Inteligencia Artificial  
**Proyecto:** UPG-LIFE (Plataforma de Mapeo Interactivo y Monitoreo Ambiental)  
**Integrantes:** Arely Rodríguez Vargas, Eder Nieto Aguilar  

## 1. MÉTODOS (Técnicas Sistemáticas de Desarrollo)
- **Modelo de Proceso:** Desarrollo Incremental y Ágil (basado en Sommerville Cap. 2 y 3), estructurado en iteraciones para la integración progresiva del hardware IoT (ESP32) y la plataforma web.
- **Técnicas de Análisis y Especificación:** Historias de Usuario orientadas a la navegación pública sin registro y a la visualización de métricas ambientales (humedad, ruido y temperatura).
- **Técnicas de Validación:** Pruebas Unitarias para la ingesta/procesamiento de datos e interfaz pública, sumado a Revisiones e Inspecciones de pares del código y firmware.

## 2. HERRAMIENTAS (Soporte Automatizado CASE y Entorno de Desarrollo)
- **Entorno Integrado (IDE):** Visual Studio Code (v1.85+) con extensiones para desarrollo Web y C++/PlatformIO (ESP32).
- **Control de Versiones y SCM:** Git CLI local y GitHub Remote Repository.
- **Analizador Estático de Código (Linter):** Flake8 / Pylint (Python) y ESLint / Cppcheck según el módulo.
- **Gestión de Tareas:** Tablero Kanban en GitHub Projects.

## 3. PROCEDIMIENTOS (Estructura y Normativa Organizacional)
- **Formato de Commits:** Convención Imperativa (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`).
- **Estrategia de Ramas (Branching):** Prohibido hacer push directo a `main`. Todo cambio se realiza en `feature/*` o `fix/*` y requiere Pull Request.
- **Política de Code Review:** Todo Pull Request requiere la revisión y aprobación escrita del integrante par antes del Merge.
