## Biblioteca API - README.md

### Descripción

Este proyecto proporciona una aplicación Flask dockerizada para una API de biblioteca.

### Requisitos previos

- Docker: Asegúrese de tener Docker instalado y funcionando en su sistema. Puede descargarlo e instalarlo desde el sitio web oficial.

### Configuración

#### 1. Clonar el repositorio

```bash
git clone https://github.com/KenethUrrutia/BIBLIOTECA_API.git
cd BIBLIOTECA_API
```

#### 2. Ejecuta el script de MySQL

Ejecuta el script de MySQL ubicado en `/db/sql/script.sql` para crear la base de datos BIBLIOTECADB

#### 3. Crear un archivo `.env`

Cree un archivo llamado `.env` en el directorio raíz del proyecto. Este archivo almacenará variables de entorno sensibles como cadenas de conexión de bases de datos y claves secretas. Aquí hay una plantilla con marcadores de posición:

```
# Cadenas de conexión de base de datos (reemplace con sus valores reales)
DEV_DATABASE_URL=mysql://root:su_contraseña@localhost:3036/BIBLIOTECADB
PROD_DATABASE_URL=mysql://root:su_contraseña@x.x.x.x:3036/BIBLIOTECADB
TEST_DATABASE_URL=mysql://root:su_contraseña@x.x.x.x:3036/BIBLIOTECADBTEST

# Clave secreta (reemplace con una cadena aleatoria segura)
SECRET_KEY='su_clave_secreta'

```

**Importante:**

- Reemplace `su_contraseña` con la contraseña real de su base de datos MySQL.
- Reemplace `su_clave_secreta` con una cadena aleatoria segura para proteger su API.

### Construcción y ejecución del contenedor Docker

#### 1. Crear la imagen Docker

```bash
docker build -t bibliotecaapi:1.0 .
```

Este comando crea una imagen Docker llamada `bibliotecaapi:1.0` utilizando el Dockerfile en el directorio actual (`.`).

#### 2. Ejecutar el contenedor

```bash
docker run -d --name api_biblioteca -p 5001:5000 bibliotecaapi:1.0
```

Este comando ejecuta la imagen `bibliotecaapi:1.0` en modo desprendido (`-d`) y asigna un nombre (`api_biblioteca`) al contenedor. También mapea el puerto 5000 del contenedor al puerto 5001 de su host (`-p 5001:5000`), lo que le permite acceder a la API en `http://localhost:5001`.

### Variables de entorno

La aplicación utiliza variables de entorno para configurar su comportamiento según el entorno elegido. El archivo `.env` que creó anteriormente establece estas variables.

#### Entorno de desarrollo

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
```

Estas configuraciones habilitan las funciones de depuración y hacen que la aplicación sea más adecuada para el desarrollo.

#### Entorno de producción

```bash
export FLASK_APP=app.py
export FLASK_ENV=production
export FLASK_DEBUG=0
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
```

Estas configuraciones deshabilitan la depuración y optimizan la aplicación para la implementación en producción.

#### Entorno de pruebas

```bash
export FLASK_APP=app.py
export FLASK_ENV=testing
export FLASK_TESTING=1
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
```

Estas configuraciones habilitan las funciones de prueba unitaria para realizar pruebas exhaustivas de la aplicación.

### Notas adicionales

- Recuerde reemplazar los marcadores de posición en el archivo `.env` con sus valores reales.
- Puede ajustar el puerto expuesto del contenedor (`-p 5001:5000`) si es necesario.
- Para un uso más avanzado, considere usar Docker Compose para administrar varios contenedores y sus dependencias.
