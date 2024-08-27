# Desarrollo de Aplicación Web para Centro Hospitalario

## Introducción

### Descripción
Este proyecto consiste en el desarrollo de una aplicación web para un centro hospitalario, con un enfoque principal en la gestión de ortesis. La aplicación está diseñada para facilitar la administración y el seguimiento de pacientes que requieren tratamiento con ortesis, así como para mejorar la comunicación y coordinación entre terapeutas y pacientes.

### Características
- **Gestión de Usuarios**:
  - **Administrador**: Permite gestionar la información de los terapeutas y pacientes, incluyendo la asignación de terapeutas a pacientes.
  - **Terapeutas**: Pueden gestionar la información de sus pacientes y realizar seguimientos relacionados con el tratamiento de ortesis.

- **Conexión con Aplicación Móvil**: La aplicación web se integra con una aplicación móvil para facilitar la comunicación y la actualización de la información de los pacientes en tiempo real.

### Lenguajes de desarrollo
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original-wordmark.svg" />

## Instrucciones de Instalación

1. **Configuración del Entorno Virtual**:
   - Asegúrate de tener Miniconda3 instalado en tu sistema.
   - Crea un entorno virtual con Miniconda utilizando el siguiente comando:
     ```bash
     conda create --name nombre-del-entorno python=3.12
     ```
   - Activa el entorno virtual:
     ```bash
     conda activate nombre-del-entorno
     ```

2. **Instalación de Dependencias**:
   - Con el entorno virtual activado, instala las dependencias del proyecto ejecutando el siguiente comando:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuración Adicional**:
   - Si el proyecto requiere configuraciones adicionales (como variables de entorno, bases de datos, etc.), consulta el archivo `README.md` para más detalles o sigue las instrucciones específicas proporcionadas en el proyecto.

## Uso

1. **Ejecutar el Servidor de Desarrollo**:
   - Con el entorno virtual activado y las dependencias instaladas, ejecuta el servidor de desarrollo con:
     ```bash
     python manage.py runserver
     ```
   - Accede a la aplicación web en tu navegador en `http://localhost:8000`.

## Contribuciones

Todos los miembros del equipo trabajan directamente en la rama principal `origin/main`. Por lo tanto, sigue estos pasos para contribuir:

1. **Clonar el Repositorio**:
   - Clona el repositorio a tu máquina local:
     ```bash
     git clone https://github.com/usuario/repositorio.git
     ```

2. **Actualizar la Rama Principal**:
   - Antes de hacer cambios, asegúrate de que tu rama local esté actualizada con la rama principal remota:
     ```bash
     git checkout main
     git pull origin main
     ```

3. **Realizar Cambios**:
   - Realiza las modificaciones necesarias en tu entorno local.

4. **Confirmar Cambios**:
   - Agrega tus cambios a la zona de preparación y confirma con un mensaje claro y descriptivo:
     ```bash
     git add .
     git commit -m "Descripción de los cambios"
     ```

5. **Sincronizar con la Rama Principal Remota**:
   - Asegúrate de que tu rama local esté actualizada antes de hacer un push. Primero, realiza un pull para obtener los últimos cambios:
     ```bash
     git pull origin main
     ```
   - Luego, envía tus cambios al repositorio remoto:
     ```bash
     git push origin main
     ```

6. **Revisión y Aprobación**:
   - Asegúrate de que todos los cambios estén revisados y aprobados por el equipo antes de hacer un push a `origin/main`. Coordina con los miembros del equipo para evitar conflictos y garantizar que el código esté listo para la integración.

## Buenas Prácticas para Commits

Escribir buenos mensajes de commit es crucial para mantener un historial de proyecto claro y comprensible. Aquí te presentamos 6 reglas para escribir un buen mensaje de commit:

1. **Usa el Verbo Imperativo**:
   - Usa verbos en presente (imperativo) como `Add`, `Change`, `Fix`, `Remove`. Esto describe claramente la acción que realiza el commit. Ejemplo:
     - Correcto: `Add new search feature`
     - Incorrecto: `Added new search feature`

2. **No Uses Punto Final ni Puntos Suspensivos**:
   - Los mensajes de commit no deben terminar con puntos finales ni puntos suspensivos. Usa un formato limpio y directo. Ejemplo:
     - Correcto: `Fix a problem with the topbar`
     - Incorrecto: `Fix a problem with the topbar...`

3. **Usa Máximo 50 Caracteres para el Mensaje de Commit**:
   - Mantén los mensajes de commit concisos. Si necesitas explicar más, usa el cuerpo del mensaje de commit. Ejemplo:
     - Correcto: `Add new search feature`
     - Incorrecto: `Add new search feature and change typography to improve performance`

4. **Añade Todo el Contexto Necesario en el Cuerpo del Mensaje**:
   - Para mensajes que requieren más detalle, usa el cuerpo del mensaje de commit para proporcionar contexto adicional. Utiliza un editor de texto si es necesario para escribir un mensaje claro.

5. **Usa un Prefijo para Tus Commits para Hacerlos Más Semánticos**:
   - Añade prefijos para clasificar los commits. Por ejemplo:
     - `feat: add new search feature`
     - `fix: remove wrong color`
   - Esto facilita la lectura y el seguimiento del historial de cambios.
   - Estos serían los prefijos:

     - `feat`: Una nueva característica para el usuario.
     - `fix`: Arregla un bug que afecta al usuario.
     - `perf`: Cambios que mejoran el rendimiento del sitio.
     - `build`: Cambios en el sistema de build, tareas de despliegue o instalación.
     - `ci`: Cambios en la integración continua.
     - `docs`: Cambios en la documentación.
     - `refactor`: Refactorización del código como cambios de nombre de variables o funciones.
     - `style`: Cambios de formato, tabulaciones, espacios o puntos y coma, etc; no afectan al usuario.
     - `test`: Añade tests o refactoriza uno existente.

## Notas Adicionales
- **Mantén Tu Rama Actualizada**: Es crucial mantener tu copia local actualizada con los últimos cambios de `origin/main` para evitar conflictos.
- **Pruebas**: Realiza pruebas exhaustivas antes de enviar tus cambios para asegurar que no introduzcan errores o problemas en el proyecto.
