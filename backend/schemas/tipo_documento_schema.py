from pydantic import BaseModel

class TipoDocumentoBase(BaseModel):
    descripcion: str

class TipoDocumentoCreate(TipoDocumentoBase):
    pass

class TipoDocumentoUpdate(BaseModel):
    descripcion: str | None = None

class TipoDocumentoOut(BaseModel):
    id_tipo_documento: int
    descripcion: str
    class Config:
        orm_mode = True