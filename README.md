# Liquidation Calculator

Aplicación web para calcular liquidaciones laborales, compuesta por un backend en FastAPI y un frontend en React, ambos ejecutados mediante Docker Compose.  La base de datos se aloja en un contenedor local de MySQL.

---

## Tecnologías principales

- React — Frontend (interfaz web)
- FastAPI — Backend (API REST)
- MySQL (Contenedor Docker) — Base de datos local
- Docker & Docker Compose — Contenedores
- Docker Hub — Almacenamiento de imágenes
- Prometheus — Herramienta de monitoreo y recolección de métricas.
- Grafana — Plataforma de visualización de métricas y dashboards.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener:

- Docker Desktop instalado y en ejecución
- Una cuenta gratuita en [https://neon.tech](https://neon.tech) para la base de datos
- (Opcional) Git, si vas a clonar el repositorio desde GitHub

---

## 1. Clonar el proyecto

```bash
git clone "https://github.com/emmanuelcalad0615/liquidationCalculator-core.git"
cd liquidationcalculator-core
```
## 2. Crear la base de datos en contenedor local MySQL

NO ES NECESARIO CREAR UNA CUENTA EXTERNA. La base de datos se creará automáticamente en un contenedor local de MySQL usando Docker Compose.


## 3. Crear el archivo .env en /backend
### Crea un archivo llamado .env dentro de la carpeta backend/ con el siguiente contenido:
```bash

SECRET_KEY = "clave_secreta_mi_hermanito"
FRONTEND_URL=["http://localhost:3000", "http://127.0.0.1:3000"]
DATABASE_URL="mysql+pymysql://root:Joaco06151970@mysql_db:3306/liquidation
```
## 4. Ejecutar la aplicación con Docker Compose
### Desde la raíz del proyecto (donde está docker-compose.yml), ejecuta:

```bash
docker compose up -d
```
Esto hará lo siguiente:

- Descargar las imágenes desde Docker Hub:

-  emmanuecalad/liquidation-calculator-backend

- emmanuecalad/liquidation-calculator-frontend

- Crear los contenedores

- Levantar automáticamente el backend y el frontend

# 5. Acceder a la aplicación
- Frontend (React): http://localhost:3000

- Backend (FastAPI Docs): http://localhost:8000/docs

## 6. Comandos útiles de Docker
### Ver contenedores activos:

```bash
docker ps
```
### Detener la aplicación:

```bash
docker compose down
```
### Ver logs del backend:

```bash

docker logs backend_app
```
### Ver logs del frontend:

```bash
docker logs frontend_app
```
## 7. Variables importantes
- Variable	Descripción	Ubicación
- DATABASE_URL	URL de conexión a MySql	backend/.env
- SECRET_KEY	Clave secreta del backend	backend/.env
- FRONTEND_URL	URLs permitidas para CORS	backend/.env
- REACT_APP_API_URL	URL interna del backend para el frontend	docker-compose.yml

##8. Estructura del proyecto
```bash
liquidationcalculator-core/
│
├── kube/ # Configuraciones de Kubernetes (Deployments, Services, etc.)
│   ├── backend-deployment.yaml
│   ├── configmap.yaml
│   ├── frontend-deployment.yaml
│   ├── grafana-deployment.yaml
│   ├── mysql-deployment.yaml
│   ├── prometheus-deployment.yaml
│   ├── secret.yaml
│   └── prometheus.yaml 
│
├── backend/ # API en FastAPI
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/ # Aplicación React
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml # Orquestador de backend, frontend y MySQL
└── my.cnf # Archivo de configuración de MySQL (si aplica)
``` 
## 9. Flujo de ejecución
- El contenedor backend_app levanta la API de FastAPI en el puerto 8000.

- El contenedor frontend_app sirve la aplicación React compilada en el puerto 3000.

- El backend se comunica con la base de datos MySQL local (usando el nombre de servicio db en el DATABASE_URL).

- El frontend consume los endpoints del backend usando la variable REACT_APP_API_URL.

## 10. Acceso a la Documentación de la API (Swagger)

### Una vez que el contenedor del backend esté en ejecución, la documentación interactiva generada por FastAPI se puede consultar en el navegador desde la siguiente URL:

### Swagger UI:

```bash
http://localhost:8000/docs
```

### ReDoc (documentación alternativa):
```bash
http://localhost:8000/redoc
```
## IMPORTANTE!
- Debe contemplar, que para registrar usuarios, debe hacerlo desde aquí y no desde la interfaz gráfica. Primero es necesario crear uno o más tipos de documento y posteriormente crear un usuario con alguno de los tipos de documentos previamente creados; y de esta manera, podrá porbar el login en la interfaz grafica.
- El token de acceso y la información de logueo del usuario, se está alojando en el SessionStorage del navegador por el momento.

## Créditos
### Proyecto desarrollado por: Julian Ferrer, Jorge Arenas, Mauricio Marquez y Emmanuel Calad.

## Imágenes Docker públicas:

- Backend → emmanuecalad/liquidation-calculator-backend

- Frontend → emmanuecalad/liquidation-calculator-frontend
