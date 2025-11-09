from fastapi import FastAPI
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from models.contrato import Contrato
from models.empleado import Empleado
from models.tipo_contrato import TipoContrato
from models.tipo_documento import TipoDocumento
from models.liquidacion import Liquidacion
from models.detalle_liquidacion import DetalleLiquidacion
from models.motivo_terminacion import MotivoTerminacion
from models.users import User
from routers.empleado_router import router as empleado_router
from routers.tipo_documento_router import router as tipo_documento_router
from routers.user_router import router as usuario_router
from routers.contrato_router import router as contrato_router
from routers.tipo_contrato_router import router as tipo_contrato_router
from routers.liquidacion_router import router as liquidacion_router
from routers.detalle_liquidacion_router import router as detalle_liquidacion_router
from routers.motivo_terminacion_router import router as motivo_terminacion_router
from config import settings
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

# Crear sesión manual para inicializar datos

from sqlalchemy.orm import Session
from database import engine
from models.tipo_documento import TipoDocumento
from models.tipo_contrato import TipoContrato

def init_catalogos():
    with Session(engine) as session:

        # Inicializar Tipo Documento
        if session.query(TipoDocumento).count() == 0:
            tipos_documento = [
                {"id_tipo_documento": 1, "descripcion": "Cédula de ciudadanía"},
                {"id_tipo_documento": 2, "descripcion": "Tarjeta de identidad"},
                {"id_tipo_documento": 3, "descripcion": "Cédula de extranjería"},
                {"id_tipo_documento": 4, "descripcion": "Pasaporte"},
            ]
            session.bulk_insert_mappings(TipoDocumento, tipos_documento)
            print("✅ Tabla tipo_documento inicializada.")

        else:
            print("⚠️ Tabla tipo_documento ya contenía datos.")

        # Inicializar Tipo Contrato
        if session.query(TipoContrato).count() == 0:
            tipos_contrato = [
                {"id_tipo_contrato": 1, "descripcion": "Contrato a término fijo"},
                {"id_tipo_contrato": 2, "descripcion": "Contrato a término indefinido"},
                {"id_tipo_contrato": 3, "descripcion": "Contrato por obra o labor"},
                {"id_tipo_contrato": 4, "descripcion": "Contrato de aprendizaje"},
            ]
            session.bulk_insert_mappings(TipoContrato, tipos_contrato)
            print("✅ Tabla tipo_contrato inicializada.")

        else:
            print("⚠️ Tabla tipo_contrato ya contenía datos.")

        session.commit()


# Ejecutar al iniciar la app
init_catalogos()


app = FastAPI()

app.title = "TaxCalculator"
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_url,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags="Home")
def home():
    return "Hola mundo"

app.include_router(empleado_router)
app.include_router(tipo_documento_router)
app.include_router(usuario_router)
app.include_router(contrato_router)
app.include_router(tipo_contrato_router)
app.include_router(liquidacion_router)
app.include_router(detalle_liquidacion_router)
app.include_router(motivo_terminacion_router)