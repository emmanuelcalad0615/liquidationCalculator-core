# Liquidation Calculator

Aplicación web para calcular liquidaciones laborales, compuesta por un backend en FastAPI y un frontend en React, ambos ejecutados mediante Docker Compose.  
La base de datos se aloja en Neon.tech (PostgreSQL).

---

## Tecnologías principales

- React — Frontend (interfaz web)
- FastAPI — Backend (API REST)
- PostgreSQL (Neon.tech) — Base de datos en la nube
- Docker & Docker Compose — Contenedores
- Docker Hub — Almacenamiento de imágenes

---

## Requisitos previos

Antes de comenzar, asegúrate de tener:

- Docker Desktop instalado y en ejecución
- Una cuenta gratuita en [https://neon.tech](https://neon.tech) para la base de datos
- (Opcional) Git, si vas a clonar el repositorio desde GitHub

---

## 1. Clonar el proyecto

```bash
git clone https://github.com/<tu_usuario>/<tu_repositorio>.git
cd liquidationcalculator-core
2. Crear la base de datos en Neon.tech
Ingresa a https://neon.tech

Crea un nuevo proyecto PostgreSQL

Copia la cadena de conexión desde la pestaña “Connection Details”, algo como:

php-template
Copiar código
postgresql://<usuario>:<contraseña>@<host>/<base_de_datos>?sslmode=require
3. Crear el archivo .env en /backend
Crea un archivo llamado .env dentro de la carpeta backend/ con el siguiente contenido:

env
Copiar código
DATABASE_URL="postgresql://neondb_owner:npg_4txuEmzGh7vo@ep-summer-unit-adlch0k8-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
SECRET_KEY="clave_secreta_mi_hermanito"
FRONTEND_URL=["http://localhost:3000", "http://127.0.0.1:3000"]
4. Ejecutar la aplicación con Docker Compose
Desde la raíz del proyecto (donde está docker-compose.yml), ejecuta:

bash
Copiar código
docker compose up -d
Esto hará lo siguiente:

Descargar las imágenes desde Docker Hub:

emmanuecalad/liquidation-calculator-backend

emmanuecalad/liquidation-calculator-frontend

Crear los contenedores

Levantar automáticamente el backend y el frontend

5. Acceder a la aplicación
Frontend (React): http://localhost:3000

Backend (FastAPI Docs): http://localhost:8000/docs

6. Comandos útiles de Docker
Ver contenedores activos:

bash
Copiar código
docker ps
Detener la aplicación:

bash
Copiar código
docker compose down
Ver logs del backend:

bash
Copiar código
docker logs backend_app
Ver logs del frontend:

bash
Copiar código
docker logs frontend_app
7. Variables importantes
Variable	Descripción	Ubicación
DATABASE_URL	URL de conexión a PostgreSQL (Neon.tech)	backend/.env
SECRET_KEY	Clave secreta del backend	backend/.env
FRONTEND_URL	URLs permitidas para CORS	backend/.env
REACT_APP_API_URL	URL interna del backend para el frontend	docker-compose.yml

8. Estructura del proyecto
bash
Copiar código
liquidationcalculator-core/
│
├── backend/                   # API en FastAPI
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/                  # Aplicación React
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
└── docker-compose.yml         # Orquestador de backend y frontend
9. Flujo de ejecución
El contenedor backend_app levanta la API de FastAPI en el puerto 8000.

El contenedor frontend_app sirve la aplicación React compilada en el puerto 3000.

El backend se comunica con la base de datos PostgreSQL alojada en Neon.tech.

El frontend consume los endpoints del backend usando la variable REACT_APP_API_URL.

Créditos
Proyecto desarrollado por Emmanuel Calad.

Imágenes Docker públicas:

Backend → emmanuecalad/liquidation-calculator-backend

Frontend → emmanuecalad/liquidation-calculator-frontend

yaml
Copiar código

---

¿Quieres que te lo genere como archivo `.md` descargable para ponerlo directamente en tu carpeta del proyecto?






