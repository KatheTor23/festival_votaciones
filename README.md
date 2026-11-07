# Sistema de Votaciones – Festival de la Leyenda Vallenata 2027

## Descripción del proyecto

Aplicación web académica desarrollada con Python y Django, utilizando MySQL como sistema de gestión de bases de datos.

El sistema permite organizar las ediciones y categorías del Festival de la Leyenda Vallenata, gestionar participantes y registrar votos de usuarios autenticados, incorporando validaciones para garantizar la integridad de la información.

## Objetivo

Desarrollar una aplicación web que permita gestionar las ediciones, categorías y votaciones del festival, facilitando la participación de los usuarios mediante un sistema de registro de votos seguro y organizado.

## Tecnologías utilizadas

- Python 3.13
- Django 5.2.18
- MySQL
- HTML y CSS
- Git y GitHub
- Visual Studio Code
- mysqlclient 2.3.0
- python-dotenv 1.2.4

## Funcionalidades implementadas

- Gestión de ediciones del festival.
- Organización de categorías por edición.
- Registro, inicio y cierre de sesión de usuarios.
- Administración de información mediante Django Admin.
- Visualización de categorías y participantes.
- Registro de votos por usuarios autenticados.
- Validación para impedir votos duplicados en una misma votación.
- Posibilidad de votar en diferentes categorías.
- Validación de votaciones abiertas y cerradas.
- Validación de que la opción seleccionada pertenezca a la votación correspondiente.
- Consulta del historial personal de votaciones.
- API de consulta de categorías y participantes mediante solicitudes GET.
- Restricción de unicidad de votos a nivel de base de datos.

## Estructura principal del proyecto

```text
festival_votaciones/
├── festival/
│   ├── settings.py
│   └── urls.py
├── ediciones/
├── usuarios/
├── votaciones/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/KatheTor23/festival_votaciones.git
cd festival_votaciones
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual en Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto, junto a `manage.py`.

Agregar la variable:

```dotenv
DJANGO_SECRET_KEY=REEMPLAZAR_CON_UNA_CLAVE_SEGURA
```

Para generar una clave segura de Django:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copiar el valor generado en el archivo `.env`.

**Importante:** el archivo `.env` contiene información privada y no debe publicarse en GitHub.

### 6. Configurar MySQL

Tener instalado y en ejecución un servidor MySQL.

Crear una base de datos vacía para el proyecto y configurar en `festival/settings.py` los valores correspondientes a:

- Nombre de la base de datos (`NAME`).
- Usuario de MySQL (`USER`).
- Contraseña de MySQL (`PASSWORD`).
- Servidor (`HOST`).
- Puerto (`PORT`).

No publicar contraseñas reales en el repositorio.

### 7. Aplicar las migraciones

```bash
python manage.py migrate
```

### 8. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

### 9. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

Para acceder al panel de administración:

http://127.0.0.1:8000/admin/

## API de categorías

El proyecto implementa una API de consulta mediante el método HTTP GET.

La API devuelve información de las categorías registradas en MySQL, sus ediciones y participantes asociados, en formato JSON.

**Ruta prevista para la entrega:**

```text
GET /api/categorias/
```

La implementación se encuentra en:

- `votaciones/views.py` → función `api_categorias`.
- `votaciones/urls.py` → configuración de rutas de la aplicación.
- `festival/urls.py` → configuración de rutas principales.

La ruta debe comprobarse en la configuración principal antes de utilizarla en la entrega.

## Validaciones y seguridad

El sistema incorpora diferentes
