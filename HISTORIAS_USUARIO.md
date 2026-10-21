# Inventario de Historias de Usuario - Proyecto Final

## Historia de Usuario HU-01: Registro de usuario

* **ID:** HU-01
* **Nombre:** Registro de usuario
* **Como:** Usuario
* **Quiero:** Registrarme en el sistema
* **Para:** Poder acceder a las funciones disponibles para los usuarios registrados
* **Estimación (Story Points):** 5
* **Prioridad:** Alta
* **Criterios de Aceptación (Gherkin):**

  * **Escenario 1:** **Dado que** el usuario proporciona sus datos correctamente, **Cuando** selecciona la opción de registrarse, **Entonces** el sistema crea su cuenta y muestra un mensaje de registro exitoso.
  * **Escenario 2:** **Dado que** el usuario proporciona datos incompletos o inválidos, **Cuando** intenta registrarse, **Entonces** el sistema muestra un mensaje indicando los datos que debe corregir.

## Historia de Usuario HU-02: Inicio de sesión

* **ID:** HU-02
* **Nombre:** Inicio de sesión
* **Como:** Usuario registrado
* **Quiero:** Iniciar sesión en el sistema
* **Para:** Acceder a las funciones disponibles para mi cuenta
* **Estimación (Story Points):** 3
* **Prioridad:** Alta
* **Criterios de Aceptación (Gherkin):**

  * **Escenario 1:** **Dado que** el usuario tiene credenciales válidas, **Cuando** ingresa su usuario y contraseña, **Entonces** el sistema permite el acceso.
  * **Escenario 2:** **Dado que** el usuario proporciona credenciales incorrectas, **Cuando** intenta iniciar sesión, **Entonces** el sistema muestra un mensaje de error.

## Historia de Usuario HU-03: Consulta de información

* **ID:** HU-03
* **Nombre:** Consulta de información
* **Como:** Usuario
* **Quiero:** Consultar la información disponible en el sistema
* **Para:** Encontrar información que necesito
* **Estimación (Story Points):** 3
* **Prioridad:** Alta
* **Criterios de Aceptación (Gherkin):**

  * **Escenario 1:** **Dado que** el usuario ha ingresado al sistema, **Cuando** selecciona una sección de información, **Entonces** el sistema muestra el contenido correspondiente.
  * **Escenario 2:** **Dado que** una sección no contiene información disponible, **Cuando** el usuario la consulta, **Entonces** el sistema muestra un mensaje indicando que no hay información disponible.

## Historia de Usuario HU-04: Consulta de perfil

* **ID:** HU-04
* **Nombre:** Consulta de perfil
* **Como:** Usuario registrado
* **Quiero:** Consultar mi información de perfil
* **Para:** Verificar mis datos personales registrados
* **Estimación (Story Points):** 3
* **Prioridad:** Media
* **Criterios de Aceptación (Gherkin):**

  * **Escenario 1:** **Dado que** el usuario ha iniciado sesión, **Cuando** accede a su perfil, **Entonces** el sistema muestra su información registrada.
  * **Escenario 2:** **Dado que** el usuario no ha iniciado sesión, **Cuando** intenta acceder al perfil, **Entonces** el sistema solicita que inicie sesión.

## Historia de Usuario HU-05: Consulta de documentos

* **ID:** HU-05
* **Nombre:** Consulta de documentos
* **Como:** Usuario
* **Quiero:** Consultar los documentos disponibles
* **Para:** Obtener la información o documentación que necesito
* **Estimación (Story Points):** 5
* **Prioridad:** Media
* **Criterios de Aceptación (Gherkin):**

  * **Escenario 1:** **Dado que** el usuario ha iniciado sesión, **Cuando** selecciona la sección de documentos, **Entonces** el sistema muestra los documentos disponibles.
  * **Escenario 2:** **Dado que** no existen documentos disponibles, **Cuando** el usuario consulta la sección, **Entonces** el sistema muestra un mensaje indicando que no hay documentos disponibles.

## Historia de Usuario HU-06: Consulta de información de contacto

* **ID:** HU-06
* **Nombre:** Consulta de contacto
* **Como:** Usuario
* **Quiero:** Consultar los datos de contacto disponibles
* **Para:** Poder comunicarme con la institución
* **Estimación (Story Points):** 1
* **Prioridad:** Baja
* **Criterios de Aceptación (Gherkin):**

  * **Escenario 1:** **Dado que** el usuario accede a la sección de contacto, **Cuando** consulta la información, **Entonces** el sistema muestra los datos de contacto disponibles.
  * **Escenario 2:** **Dado que** la información de contacto no está disponible, **Cuando** el usuario accede a la sección, **Entonces** el sistema muestra un mensaje indicando que no hay información disponible.
