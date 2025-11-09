from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.motivo_terminacion_schema import (
    MotivoTerminacionCreate,
    MotivoTerminacionOut,
    MotivoTerminacionUpdate
)
import services.motivo_terminacion_service as motivo_service


router = APIRouter(prefix="/motivo_terminacion", tags=["MotivoTerminacion"])


@router.post("/", response_model=MotivoTerminacionOut, status_code=status.HTTP_201_CREATED)
def create_motivo_route(payload: MotivoTerminacionCreate, db: Session = Depends(get_db)):
    return motivo_service.create_motivo_terminacion(db, payload)


@router.get("/", response_model=list[MotivoTerminacionOut])
def get_all_motivos_route(db: Session = Depends(get_db)):
    return motivo_service.get_all_motivos(db)


@router.get("/{id_motivo_terminacion}", response_model=MotivoTerminacionOut)
def get_motivo_route(id_motivo_terminacion: int, db: Session = Depends(get_db)):
    return motivo_service.get_motivo_by_id(db, id_motivo_terminacion)


@router.put("/{id_motivo_terminacion}", response_model=MotivoTerminacionOut)
def update_motivo_route(id_motivo_terminacion: int, payload: MotivoTerminacionUpdate, db: Session = Depends(get_db)):
    return motivo_service.update_motivo_terminacion(db, id_motivo_terminacion, payload)


@router.delete("/{id_motivo_terminacion}", status_code=status.HTTP_204_NO_CONTENT)
def delete_motivo_route(id_motivo_terminacion: int, db: Session = Depends(get_db)):
    motivo_service.delete_motivo_terminacion(db, id_motivo_terminacion)
