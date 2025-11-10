from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class DetalleLiquidacionOut(BaseModel):
    id_detalle: int
    concepto: str
    valor: float

    class Config:
        orm_mode = True


class MotivoTerminacionOut(BaseModel):
    id_motivo_terminacion: int
    descripcion: str

    class Config:
        orm_mode = True


class LiquidacionBase(BaseModel):
    id_contrato: int
    fecha_liquidacion: date
    id_motivo_terminacion: int
    total_liquidacion: float


class LiquidacionCreate(LiquidacionBase):
    pass


class LiquidacionUpdate(BaseModel):
    id_contrato: Optional[int] = None
    fecha_liquidacion: Optional[date] = None
    id_motivo_terminacion: Optional[int] = None
    total_liquidacion: Optional[float] = None


class LiquidacionOut(BaseModel):
    id_liquidacion: int
    id_contrato: int
    fecha_liquidacion: date
    id_motivo_terminacion: int
    total_liquidacion: float
    motivo_terminacion: Optional[MotivoTerminacionOut]
    detalles_liquidacion: List[DetalleLiquidacionOut] = []

    class Config:
        orm_mode = True

