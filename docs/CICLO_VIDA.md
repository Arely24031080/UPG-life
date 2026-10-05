# ANÁLISIS DEL CICLO DE VIDA

## 1. Mapeo de Fases Clásicas (Modelo en Cascada / Incremental)

1. **Requerimientos y Análisis:**
   Identificar las necesidades del sistema, definir el funcionamiento del sensor PIR, la ESP32-CAM y el sistema web. También se definirán los datos que deberán registrarse en cada evento.

2. **Diseño de Arquitectura y Base de Datos:**
   Diseñar la comunicación entre el sensor PIR y la ESP32-CAM, así como la estructura del sistema web y el almacenamiento de las fotografías, fechas y horas de los eventos.

3. **Implementación / Codificación:**
   Programar la ESP32-CAM para recibir la señal del sensor PIR y capturar fotografías. Desarrollar también el sistema web para registrar y consultar los eventos.

4. **Pruebas y Verificación:**
   Realizar pruebas para comprobar que el sensor detecte correctamente el movimiento, que la ESP32-CAM capture la fotografía y que el evento se registre con su fecha y hora. También se verificará la consulta del historial desde el sistema web.

5. **Mantenimiento y Evolución:**
   Corregir errores encontrados durante las pruebas y realizar mejoras al sistema conforme se identifiquen nuevas necesidades.

## 2. Aplicación de los Modelos de Desarrollo

### Modelo en Cascada

El modelo en cascada permitirá organizar el desarrollo del proyecto mediante fases consecutivas, comenzando con los requerimientos y continuando con el diseño, implementación, pruebas y mantenimiento.

### Modelo Incremental

El proyecto podrá desarrollarse mediante incrementos, agregando y probando funcionalidades de manera progresiva. Por ejemplo, primero se puede implementar la detección de movimiento, después la captura de fotografías y posteriormente el registro y consulta de los eventos mediante el sistema web.

### Modelo en Espiral

El modelo en espiral permitirá considerar los riesgos del proyecto durante las diferentes etapas de desarrollo, especialmente los relacionados con la comunicación entre los componentes, la captura de fotografías y el almacenamiento de los eventos.