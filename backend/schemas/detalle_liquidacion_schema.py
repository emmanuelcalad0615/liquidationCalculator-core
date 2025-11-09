from pydantic import BaseModel
from decimal import Decimal


class DetalleLiquidacionBase(BaseModel):
    concepto: str
    valor: Decimal


class DetalleLiquidacionCreate(DetalleLiquidacionBase):
    id_liquidacion: int


class DetalleLiquidacionUpdate(BaseModel):
    concepto: str | None = None
    valor: Decimal | None = None


class DetalleLiquidacionOut(BaseModel):
    id_detalle: int
    id_liquidacion: int
    concepto: str
    valor: Decimal

    class Config:
        orm_mode = True
