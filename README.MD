# Prueba Técnica Full-Stack: FastAPI + PostgreSQL + Vue 3

Proyecto desarrollado para evaluación técnica. Consiste en una aplicación web full-stack modular para la gestión de registros (ítems), utilizando FastAPI en el backend, PostgreSQL como base de datos relacional y Vue 3 (Composition API) con Vite en el frontend.

## Arquitectura del Proyecto

```text
├── backend/
│   ├── main.py          # Definición de endpoints FastAPI y esquemas Pydantic
│   ├── database.py      # Configuración de SQLAlchemy y gestión de sesión
│   ├── models.py        # Modelos ORM / Tablas PostgreSQL
│   ├── requirements.txt # Dependencias de Python
│   └── .env             # Variables de entorno (DATABASE_URL)
├── frontend/
│   ├── src/
│   │   ├── components/  # Componentes reutilizables (ItemForm.vue, ItemList.vue)
│   │   ├── services/    # Módulo de peticiones HTTP (api.js)
│   │   ├── App.vue      # Vista principal
│   │   └── style.css    # Estilos globales
│   ├── package.json     # Dependencias de Node
│   └── .env             # Variables de entorno (VITE_API_URL)
├── package.json         # Ejecución concurrente del entorno de desarrollo
└── README.md

Requisitos Previos

    Python 3.10+

    Node.js 18+

    PostgreSQL activo localmente o mediante servidor remoto.

Configuración del Entorno
1. Variables de Entorno

Crear el archivo backend/.env:
Fragmento de código

DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_bd

Crear el archivo frontend/.env:
Fragmento de código

VITE_API_URL=http://localhost:8000

2. Instalación de Dependencias

Backend (Python):
Bash

cd backend
python -m venv venv
# En Linux/macOS:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate

pip install -r requirements.txt

Frontend (Node):
Bash

cd frontend
npm install

Raíz (Para desarrollo simultáneo):
Bash

npm install

Ejecución del Proyecto

Para levantar tanto el backend como el frontend de forma simultánea desde la raíz:
Bash

npm run dev

    Frontend: http://localhost:5173

    Backend API: http://localhost:8000

    Documentación Swagger: http://localhost:8000/docs