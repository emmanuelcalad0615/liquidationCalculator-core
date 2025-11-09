from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.tipo_contrato_schema import TipoContratoCreate, TipoContratoOut, TipoContratoUpdate
import services.tipo_contrato_service as tipo_contrato_service

router = APIRouter(prefix="/tipo_contrato", tags=["TipoContrato"])

@router.post("/", response_model=TipoContratoOut, status_code=status.HTTP_201_CREATED)
def create_tipo_contrato_route(payload: TipoContratoCreate, db: Session = Depends(get_db)):
    return tipo_contrato_service.create_tipo_contrato(db, payload)


@router.get("/", response_model=list[TipoContratoOut])
def get_all_tipo_contratos_route(db: Session = Depends(get_db)):
    return tipo_contrato_service.get_all_tipo_contratos(db)


@router.get("/{id_tipo_contrato}", response_model=TipoContratoOut)
def get_tipo_contrato_by_id_route(id_tipo_contrato: int, db: Session = Depends(get_db)):
    return tipo_contrato_service.get_tipo_contrato_by_id(db, id_tipo_contrato)


@router.put("/{id_tipo_contrato}", response_model=TipoContratoOut)
def update_tipo_contrato_route(id_tipo_contrato: int, payload: TipoContratoUpdate, db: Session = Depends(get_db)):
    return tipo_contrato_service.update_tipo_contrato(db, id_tipo_contrato, payload)


@router.delete("/{id_tipo_contrato}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tipo_contrato_route(id_tipo_contrato: int, db: Session = Depends(get_db)):
    tipo_contrato_service.delete_tipo_contrato(db, id_tipo_contrato)
