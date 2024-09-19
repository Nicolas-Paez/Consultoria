# Desarrollo de Aplicación Web para Centro Hospitalario
![Hospital roberto del rio](https://github.com/user-attachments/assets/e07cab5f-f41e-4464-8a08-c2e808d71ed7)
## Introducción

### Descripción
Este proyecto consiste en el desarrollo de una aplicación web para un centro hospitalario, con un enfoque principal en la gestión de ortesis. La aplicación está diseñada para facilitar la administración y el seguimiento de pacientes que requieren tratamiento con ortesis, así como para mejorar la comunicación y coordinación entre terapeutas y pacientes.

### Características
- **Gestión de Usuarios**:
  - **Administrador**: Permite gestionar la información de los terapeutas y pacientes, incluyendo la asignación de terapeutas a pacientes.
  - **Terapeutas**: Pueden gestionar la información de sus pacientes y realizar seguimientos relacionados con el tratamiento de ortesis.

- **Conexión con Aplicación Móvil**: La aplicación web se integra con una aplicación móvil para facilitar la comunicación y la actualización de la información de los pacientes en tiempo real.

### Lenguajes de desarrollo
<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="60" height="60" style="margin-right: 50px;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain-wordmark.svg" width="60" height="60" style="margin-right: 50px;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="60" height="60" style="margin-right: 50px;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" width="60" height="60" style="margin-right: 50px;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" width="60" height="60" style="margin-right: 50px;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original-wordmark.svg" width="60" height="60" style="margin-right: 50px;"/>
</p>

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

## Requisitos de PostgreSQL

Para esta versión de Django (5.1), se debe usar PostgreSQL 13 o superior. La versión recomendada es PostgreSQL 16.4.

## Uso

1. **Ejecutar el Servidor de Desarrollo**:
   - Con el entorno virtual activado y las dependencias instaladas, ejecuta el servidor de desarrollo con:
     ```bash
     python manage.py runserver
     ```
   - Accede a la aplicación web en tu navegador en `http://localhost:8000`.

## Contribuciones

Para contribuir al proyecto, sigue estos pasos:

1. **Clonar el Repositorio**:
   - Clona el repositorio a tu máquina local:
     ```bash
     git clone https://github.com/usuario/repositorio.git
     ```

2. **Crear una Rama Nueva**:
   - Antes de hacer cambios, crea una rama nueva a partir de la rama principal `main` para trabajar en tu tarea o característica:
     ```bash
     git checkout -b nombre-de-la-rama
     ```
   - Usa nombres descriptivos para la rama, por ejemplo:
     - `feature/nueva-funcionalidad`
     - `bugfix/corregir-error`

3. **Realizar Cambios**:
   - Realiza las modificaciones necesarias en tu entorno local en la rama que has creado.

4. **Confirmar Cambios**:
   - Agrega tus cambios a la zona de preparación y confirma con un mensaje claro y descriptivo:
     ```bash
     git add .
     git commit -m "Descripción de los cambios"
     ```

5. **Actualizar Tu Rama**:
   - Asegúrate de que tu rama esté actualizada con los últimos cambios de `main` antes de hacer un push:
     ```bash
     git pull origin main
     ```

6. **Sincronizar con la Rama Principal Remota**:
   - Envía tus cambios al repositorio remoto:
     ```bash
     git push origin nombre-de-la-rama
     ```

7. **Crear un Pull Request**:
   - Ve a GitHub y crea un Pull Request (PR) para solicitar la integración de tus cambios en la rama `main`. Asegúrate de proporcionar una descripción clara del propósito del PR y cualquier información relevante.

8. **Revisión y Aprobación**:
   - Los miembros del equipo revisarán tu PR. Asegúrate de responder a los comentarios y realizar ajustes si es necesario. Una vez aprobado, tu PR será fusionado a la rama `main`.

9. **Eliminar la Rama**:
   - Después de que tu PR haya sido fusionado, puedes eliminar la rama que creaste para mantener el repositorio limpio:
     ```bash
     git branch -d nombre-de-la-rama
     git push origin --delete nombre-de-la-rama
     ```

10. **Mantener la Rama Actualizada**:
    - Si estás trabajando en una rama de larga duración, asegúrate de mantenerla actualizada con la rama `main` para evitar conflictos y asegurar la compatibilidad con los últimos cambios.

## Buenas Prácticas para Ramas en Git

Aquí están las convenciones para trabajar con ramas en Git:

1. **Rama principal (`main` o `master`)**:
   - **Propósito**: Rama estable y lista para producción.
   - **Uso**: Solo se fusiona código probado y aprobado.

2. **Ramas de características (`feature`)**:
   - **Convención**: `feature/nueva-funcionalidad`
   - **Uso**: Para nuevas funcionalidades.

3. **Ramas de corrección de errores (`bugfix`)**:
   - **Convención**: `bugfix/corregir-error`
   - **Uso**: Para solucionar errores.

4. **Ramas de desarrollo (`develop`)**:
   - **Propósito**: Integrar trabajo en progreso antes de producción.
   - **Uso**: Todas las características y correcciones antes de `main`.

5. **Ramas de hotfix (`hotfix`)**:
   - **Convención**: `hotfix/corregir-crash`
   - **Uso**: Para correcciones críticas en producción.

6. **Ramas de versión (`release`)**:
   - **Convención**: `release/version`
   - **Uso**: Preparar una nueva versión para producción.

7. **Nombres descriptivos**:
   - Nombres claros y concisos para cada rama.

8. **Separación de contextos**:
   - Mantén ramas específicas para cada tarea.

9. **Eliminar ramas innecesarias**:
   - Elimina ramas después de fusionarlas si ya no son necesarias.

10. **Uso de Pull Requests**:
    - Revisa el código antes de fusionar a `main` o `develop`.

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
