# 1️⃣ Imagen base ligera
FROM python:3.11-slim

# 2️⃣ Evitar buffers y archivos pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Crear carpeta de trabajo
WORKDIR /app

# 4️⃣ Copiar requirements
COPY requirements.txt .

# 5️⃣ Instalar dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 6️⃣ Copiar todo el backend
COPY . .

# 7️⃣ Exponer puerto
EXPOSE 8000

# 8️⃣ Comando para ejecutar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
