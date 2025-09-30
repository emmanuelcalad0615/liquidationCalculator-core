from fastapi import FastAPI
from database import engine, Base
from models.contrato import Contrato
from models.empleado import Empleado
from models.tipo_contrato import TipoContrato
from models.tipo_documento import TipoDocumento
from models.liquidacion import Liquidacion
from models.detalle_liquidacion import DetalleLiquidacion
from models.motivo_terminacion import MotivoTerminacion

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.title = "TaxCalculator"

@app.get("/", tags="Home")
def home():
    return "Hola mundo"