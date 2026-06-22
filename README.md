# TeamTransit

## Sistema de visualización de vuelos y alojamientos de las selecciones del Mundial 2026

---

## Integrantes

* Lautaro Tonini
* Fabrizio Rossato
* Adriano Oyola
* Gregorio Bizzotto

---

## Descripción

**TeamTransit** es una aplicación web que permite visualizar los vuelos y alojamientos de las selecciones participantes de la Copa Mundial de la FIFA 2026.

Los usuarios pueden consultar:

* Estadios de destino de cada selección.
* Fechas y horarios de los vuelos.
* Información sobre los alojamientos y hoteles donde se hospedan los equipos.
* Ciudades sede en México, Canadá y Estados Unidos.

El objetivo del proyecto es centralizar y presentar de forma clara la logística de transporte y estadía de las selecciones durante el torneo.

---

## Configuración de la Base de Datos

Antes de ejecutar la aplicación, configura las siguientes variables de entorno:

```env
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base>
MYSQL_PORT=<puerto_mysql>
MYSQL_HOST=<host_mysql>
MAIL_USERNAME = <Email>
MAIL_PASSWORD = <contraseña (app password)>
SECRET_KEY = <usualmente, contraseña de 32 digitos>
```

---

## Ejecución del Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/adrianoop03/vuelos_estadia.git
```

### 2. Ingresar al directorio del proyecto

```bash
cd vuelos_estadia
```
### 3. Crear Entorno virtual y activarlo

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python app.py
```
### 6. Ejecutar la seed

```bash
python seed.py
```
---

## Endpoints Implementados

### Stays

```http
GET    /stays
GET    /stays/<int:id_stays>
POST   /stays
PUT    /stays/<int:id_stays>
DELETE /stays/<int:id_stays>
```
### User

```http
GET    /user/register
POST   /user/register
GET    /user/verif/<Token>
GET    /user/login
POST   /user/login
GET    /user/index
GET    /user/admin
GET    /user/users
GET    /user/logout
GET    /user/reset-password
POST   /user/reset-password
GET,POST /user/reset/<token>
```
### Flights

```http
GET    /flights
GET    /flights/<int:id_flight>
POST   /flights
```

### Stadiums

```http
GET /stadium
GET /stadium/<int:id_stadium>
```

### Teams

```http
GET /team
GET /team/<int:id_team>
```

---

## Aportes de los Integrantes

### Lautaro Tonini

* Creación del modelo User.
* Creación y mantenimiento de `seed.py`.
* Desarrollo de rutas para usuarios y sistema de carga de usuarios.
* Desarrollo de controladores de usuarios.
* Implementación del sistema de recuperación de contraseña.
* Creación de `forgot_password.html`,`reset_password.html`.
* Edición y corrección de:

  * `login.html`
  * `register.html`
  * `flight.html`
  * `login.css`
  * `flight.css`
* Edición y corrección de `register.html`.
* Corrección de errores y compatibilidades.
* Resolución de conflictos y realización de merges entre ramas.

### Fabrizio Rossato

* Creación del modelo Stadium.
* Creación del modelo Team.
* Desarrollo de rutas para Stadium y Team.
* Desarrollo de controladores para Stadium y Team.
* Modificación y adaptación del controlador y rutas de Flight para la integración con HTML.
* Creación de:

  * `flight.html`
  * `flight.css`
* Búsqueda e inserción de imágenes de estadios en `static/img`.
* Creación y mantenimiento de la documentación y del archivo `README.md`.

### Adriano Oyola

* Creación del modelo Flight.
* Desarrollo de rutas de Flight.
* Desarrollo del controlador de Flight.
* Creación de:

  * `admin.html` `admin.css`
  * `index.html` `index.css` 
  * `login.html` `login.css`
  * `stays.html` `stays.css`
  * `users.html` `users.css`
* Modificación y adaptación de controladores y rutas para los archivos HTML mencionados.
* Búsqueda e inserción de imágenes de fondo en `static/img`.

### Gregorio Bizzotto

* Creación del modelo Stays.
* Desarrollo de rutas de Stays.
* Desarrollo del controlador de Stays.
* Modificación y adaptación del controlador y rutas de:

  * `admin.html`
  * `admin.css`
* Edición y corrección de `stays.html`,`admin.html`,`stays.css` y `admin.css`.

---

## Trabajo Grupal

* Diseño y planificación general de la aplicación.
* Desarrollo e implementación de funcionalidades.
* Investigación y documentación de datos.
* Configuración de la aplicación y la base de datos.
* Corrección de errores y pruebas.
* Integración y validación final del proyecto.

---

## Tecnologías Utilizadas

* Python
* Flask
* SQLAlchemy
* MySQL
* HTML5
* CSS3
* BootStrap 5
* Git
* GitHub
* Github Copilot
* ChatGPT
* Claude code

---

## Repositorio

```bash
https://github.com/adrianoop03/vuelos_estadia
```

