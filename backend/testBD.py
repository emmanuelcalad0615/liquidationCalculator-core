from sqlalchemy import create_engine, text
from config import settings

# pega aquí tu string completo (usa psycopg2)
DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL, echo=True)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("✅ Conexión exitosa:", result.scalar())
except Exception as e:
    print("❌ Error de conexión:", e)