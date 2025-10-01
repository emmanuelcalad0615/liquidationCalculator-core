from pydantic import BaseModel
from datetime import date 

class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: int
    documento: str
    fecha_nacimiento:date

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    nombres: str | None = None
    apellidos: str | None = None
    tipo_documento: int | None = None
    documento: str | None = None
    fecha_nacimiento: date | None = None

class EmpleadoOut(BaseModel):
    id_empleado: int
    nombres: str
    apellidos: str

    class Config:
        from_attributes = True
