from pydantic import BaseModel


class MotivoTerminacionBase(BaseModel):
    descripcion: str


class MotivoTerminacionCreate(MotivoTerminacionBase):
    pass


class MotivoTerminacionUpdate(BaseModel):
    descripcion: str | None = None


class MotivoTerminacionOut(BaseModel):
    id_motivo_terminacion: int
    descripcion: str

    class Config:
        orm_mode = True
