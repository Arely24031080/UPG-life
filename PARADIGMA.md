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

<!-- IoT & Hardware -->
![ESP32](https://img.shields.io/badge/ESP32-E6353B?style=for-the-badge&logo=espressif&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)

<!-- Software & Web -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<!-- Herramientas -->
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)