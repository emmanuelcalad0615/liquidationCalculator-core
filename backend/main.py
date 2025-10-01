from fastapi import FastAPI
from database import engine, Base
from models.contrato import Contrato
from models.empleado import Empleado
from models.tipo_contrato import TipoContrato
from models.tipo_documento import TipoDocumento
from models.liquidacion import Liquidacion
from models.detalle_liquidacion import DetalleLiquidacion
from models.motivo_terminacion import MotivoTerminacion
from routers.empleado_router import router as empleado_router
from routers.tipo_documento_router import router as tipo_documento_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.title = "TaxCalculator"

@app.get("/", tags="Home")
def home():
    return "Hola mundo"

app.include_router(empleado_router)
app.include_router(tipo_documento_router)