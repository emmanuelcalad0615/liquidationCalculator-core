from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class DetalleLiquidacionResponse(BaseModel):
    concepto: str
    valor: float


class LiquidacionBase(BaseModel):
    id_contrato: int
    id_motivo_terminacion: int


class LiquidacionRequest(LiquidacionBase):
    pass


class LiquidacionResponse(BaseModel):
    id_liquidacion: int
    fecha_liquidacion: date
    total_liquidacion: float
    detalles: List[DetalleLiquidacionResponse]

    class Config:
        orm_mode = True
