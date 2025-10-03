from pydantic import BaseModel
from datetime import date 
from pydantic import BaseModel
from typing import Optional


class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: int
    documento: str
    fecha_nacimiento:date

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    tipo_documento: Optional[int] = None
    documento: Optional[str]  = None
    fecha_nacimiento: Optional[date] = None

class EmpleadoOut(BaseModel):
    id_empleado: int
    nombres: str
    apellidos: str
    tipo_documento: int
    documento: str
    fecha_nacimiento:date

    class Config:
        from_attributes = True
