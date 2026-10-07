# Gestor de tareas: FastAPI + PostgreSQL + Vue 3

Aplicación full-stack para crear, consultar, completar y eliminar tareas. El backend usa FastAPI y SQLAlchemy; el frontend usa Vue 3 y Vite. El script de desarrollo de la raíz ejecuta el backend y el frontend en paralelo con `concurrently`.

## Requisitos

- Python 3.10 o superior
- Node.js y npm
- PostgreSQL activo

## Configuración inicial

Ejecuta estos pasos desde la raíz del repositorio.

### 1. Crear la base de datos

Si todavía no existe, créala en PostgreSQL:

```bash
createdb -U postgres mibase
```

También puedes crearla desde `psql`:

```sql
CREATE DATABASE mibase;
```

### 2. Crear la tabla

Desde la raíz del repositorio, ejecuta el esquema contra la base de datos `mibase`:

```bash
psql -U postgres -d mibase -f backend/scheme.sql
```

El esquema crea la tabla `tasks` con las columnas `id`, `title`, `priority`, `done` y `created_at`. El archivo contiene `CREATE TABLE IF NOT EXISTS`; por tanto, no cambia una tabla `tasks` que ya exista. Si ya tienes una tabla creada con nombres de columnas diferentes, debes alinearla con el modelo en `backend/models.py` antes de iniciar la aplicación.

### 3. Configurar la conexión

Crea `backend/.env` con la URL de tu PostgreSQL:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/mibase
```

Sustituye `usuario` y `contraseña` por tus credenciales. La base de datos `mibase` debe existir antes de arrancar el backend.

### 4. Instalar dependencias

Desde la raíz, prepara el entorno Python que utiliza el comando concurrente del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

Instala las dependencias del frontend y el ejecutor concurrente:

```bash
npm install --prefix frontend
npm install
```

## Iniciar backend y frontend juntos

Desde la raíz del repositorio, con el entorno virtual activado, ejecuta:

```bash
npm run dev
```

Este comando inicia ambos procesos en paralelo:

- Frontend: <http://localhost:5173>
- API backend: <http://localhost:8000>
- Documentación interactiva de FastAPI: <http://localhost:8000/docs>

Los logs se muestran identificados como `BACKEND` y `FRONTEND`. Pulsa `Ctrl+C` para detener ambos procesos. No es necesario iniciar cada servidor en otra terminal.

## Pendientes

- Añadir migraciones versionadas para actualizar tablas existentes de forma segura. `scheme.sql` sirve para crear la tabla inicial; `Base.metadata.create_all()` no modifica columnas de tablas ya creadas.
- Añadir pruebas automatizadas para los endpoints del backend y los flujos principales del frontend.
- Mover la configuración del origen CORS a una variable de entorno; actualmente el backend permite el origen local `http://localhost:5173`.

## Entregables

Incluye el código fuente, los archivos de dependencias y configuración de ejemplo, el esquema SQL y este README. No incluyas ni subas:

- Archivos `.env` con configuración local o credenciales.
- Directorios `node_modules/`.
- Entornos virtuales de Python, como `venv/` o `.venv/`.

Estos archivos y directorios están excluidos por `.gitignore`. Cada persona debe crear su propio `.env` local siguiendo las instrucciones anteriores e instalar las dependencias en su equipo.
