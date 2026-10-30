Sistema de Votaciones – Festival Vallenato

## Descripción del proyecto

Aplicación web desarrollada con Django y Python, orientada a la gestión de votaciones de el Festival Vallenato.
El sistema busca facilitar la organización de la información de el concurso y proporcionar una plataforma para administrar las votaciones y la participación de los usuarios.

## Objetivo

Desarrollar una aplicación web que permita gestionar las diferentes ediciones del festival, organizar sus categorías y apoyar el proceso de votación mediante una plataforma estructurada y accesible.

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- SQL
- Git y GitHub
- Visual Studio Code

## Funcionalidades del sistema

El proyecto contempla las siguientes funcionalidades:

- Gestión de ediciones del festival.
- Organización de categorías por edición.
- Registro e inicio de sesión de usuarios.
- Administración de información mediante Django Admin.
- Visualización de ediciones y categorías.
- Gestión de votaciones y opciones de participación.
- Registro y validación de votos (Pendiente).

Algunas funcionalidades pueden encontrarse en desarrollo.

## Estructura del proyecto

festival_votaciones/
├── festival/
│   ├── settings.py
│   └── urls.py
├── ediciones/
│   ├── templates/
│   ├── views.py
│   └── urls.py
├── usuarios/
│   ├── templates/
│   ├── forms.py
│   └── views.py
├── votaciones/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md

## Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone URL_DEL_REPOSITORIO
cd festival_votaciones
```

**2. Crear el entorno virtual**

```bash
python -m venv .venv
```

**3. Activar el entorno virtual en Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**5. Configurar la base de datos**

Configurar la conexión a la base de datos en `festival/settings.py`, según el motor utilizado en el proyecto.

**6. Aplicar las migraciones**

```bash
python manage.py migrate
```

**7. Ejecutar el servidor**

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Estado del proyecto

Proyecto académico en desarrollo, correspondiente a la implementación de una aplicación web con Django, modelos relacionales, autenticación, vistas, rutas y plantillas HTML.

## Autoría

Proyecto desarrollado como parte de una actividad académica de desarrollo web con Django.

Grupo: 
* Jenny Katherine Torres Castro 
* Jhonatan Rendón Diaz 
* Paula Andrea Hurtado Espitia 
