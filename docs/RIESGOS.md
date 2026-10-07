# MATRIZ DE EVALUACIÓN DE RIESGOS

| ID | Descripción del Riesgo | Probabilidad | Impacto | Estrategia de Mitigación |
|---|---|---|---|---|
| R-01 | El sensor PIR puede presentar fallas en la detección de movimiento. | Media | Alto | Realizar pruebas tempranas y ajustar la configuración y ubicación del sensor. |
| R-02 | La ESP32-CAM puede presentar problemas al capturar o almacenar fotografías. | Media | Alto | Realizar pruebas de captura y almacenamiento antes de integrar todo el sistema. |
| R-03 | Puede existir una falla en la comunicación entre el sensor PIR y la ESP32-CAM. | Media | Alto | Realizar pruebas de integración entre los componentes desde las primeras etapas. |
| R-04 | Retraso en el desarrollo de alguna parte del sistema por parte de los integrantes del equipo. | Media | Medio | Distribuir las actividades y realizar un seguimiento semanal mediante el tablero Kanban. |
| R-05 | Problemas en el almacenamiento o consulta de fotografías y eventos. | Media | Alto | Realizar pruebas del almacenamiento y de la consulta de los registros antes de la integración final. |
| R-06 | Cambios en los requerimientos del proyecto durante el desarrollo. | Media | Medio | Revisar y documentar los requerimientos antes de implementar nuevas funcionalidades. |