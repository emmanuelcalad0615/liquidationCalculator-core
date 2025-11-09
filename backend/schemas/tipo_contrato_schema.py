from pydantic import BaseModel

class TipoContratoBase(BaseModel):
    descripcion: str


class TipoContratoCreate(TipoContratoBase):
    pass


class TipoContratoUpdate(BaseModel):
    descripcion: str | None = None


class TipoContratoOut(BaseModel):
    id_tipo_contrato: int
    descripcion: str

    class Config:
        orm_mode = True
