from pydantic import BaseModel
from datetime import date
from typing import Optional

class ContratoBase(BaseModel):
    id_empleado: int
    id_tipo_contrato: int
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    salario_mensual: float
    auxilio_transporte: Optional[int] = None


class ContratoCreate(ContratoBase):
    pass


class ContratoUpdate(BaseModel):
    id_empleado: Optional[int] = None
    id_tipo_contrato: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    salario_mensual: Optional[float] = None
    auxilio_transporte: Optional[int] = None


class ContratoOut(BaseModel):
    id_contrato: int
    id_empleado: int
    id_tipo_contrato: int
    fecha_inicio: date
    fecha_fin: Optional[date]
    salario_mensual: float
    auxilio_transporte: Optional[int]

    class Config:
        orm_mode = True
