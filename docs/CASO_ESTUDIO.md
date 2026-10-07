# CASO DE ESTUDIO: Sistema de Monitoreo Inteligente del Aula

## 1. Definición del Problema Real

En las aulas pueden ocurrir movimientos o accesos cuando no se cuenta con una supervisión constante. Actualmente, identificar y consultar estos eventos puede resultar complicado si no existe un sistema que permita registrar de manera automática lo ocurrido dentro del aula.

El Sistema de Monitoreo Inteligente del Aula busca solucionar esta problemática mediante un sensor PIR y una ESP32-CAM. Cuando el sensor detecta movimiento, la ESP32-CAM recibe la señal y toma una fotografía. El sistema registra el evento junto con su fecha y hora, permitiendo posteriormente consultar un historial de fotografías y eventos mediante un sistema web.

## 2. Objetivos del Sistema

- **Objetivo General:** Desarrollar un sistema de monitoreo que permita detectar movimiento dentro de un aula, capturar fotografías y registrar los eventos para su consulta mediante una plataforma web.

- **Objetivos Específicos:**
  1. Detectar movimiento dentro del aula mediante un sensor PIR y enviar la señal a la ESP32-CAM.
  2. Capturar y registrar fotografías de los eventos detectados junto con su fecha y hora.
  3. Desarrollar una interfaz web que permita consultar el historial de fotografías y eventos registrados.

## 3. Actores del Sistema (Usuarios)

| Actor | Rol y Responsabilidad | Perfil Técnico | Access Level |
|---|---|---|---|
| Administrador | Gestionar y consultar los registros de eventos y fotografías del sistema. | Técnico alto | Full |
| Operador | Supervisar los eventos detectados y consultar las fotografías registradas. | Medio | Read/Write |
| Usuario Final | Consultar el historial de eventos y fotografías disponibles. | Básico | Read Only |

## 4. Alcance y Límites del Proyecto

- **Incluye:**
  - Detección de movimiento mediante un sensor PIR.
  - Comunicación entre el sensor PIR y la ESP32-CAM.
  - Captura de fotografías cuando se detecta movimiento.
  - Registro de fecha y hora de los eventos.
  - Almacenamiento de las fotografías y eventos.
  - Consulta del historial mediante un sistema web.

- **No Incluye:**
  - Reconocimiento facial.
  - Identificación automática de personas.
  - Control de acceso mediante reconocimiento biométrico.
  - Vigilancia de otras instalaciones fuera del aula.
  - Funciones de inteligencia artificial para identificar personas.