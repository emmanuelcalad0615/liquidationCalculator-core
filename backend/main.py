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
from config import settings
Base.metadata.create_all(bind=engine)

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