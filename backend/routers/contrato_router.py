from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db

from schemas.contrato_schema import ContratoCreate, ContratoOut, ContratoUpdate
import services.contrato_service as contrato_service

router = APIRouter(prefix="/contrato", tags=["Contrato"])


@router.post("/", response_model=ContratoOut, status_code=status.HTTP_201_CREATED)
def create_contrato_route(payload: ContratoCreate, db: Session = Depends(get_db)):
    return contrato_service.create_contrato(db, payload)


@router.get("/", response_model=list[ContratoOut])
def get_all_contratos_route(db: Session = Depends(get_db)):
    return contrato_service.get_all_contratos(db)


@router.get("/{id_contrato}", response_model=ContratoOut)
def get_contrato_by_id_route(id_contrato: int, db: Session = Depends(get_db)):
    return contrato_service.get_contrato_by_id(db, id_contrato)


@router.put("/{id_contrato}", response_model=ContratoOut)
def update_contrato_route(id_contrato: int, payload: ContratoUpdate, db: Session = Depends(get_db)):
    return contrato_service.update_contrato(db, id_contrato, payload)


@router.delete("/{id_contrato}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contrato_route(id_contrato: int, db: Session = Depends(get_db)):
    return contrato_service.delete_contrato(db, id_contrato)

@router.get("/empleado/{id_empleado}", response_model=list[ContratoOut])
def get_contratos_by_empleado_route(id_empleado: int, db: Session = Depends(get_db)):
    """
    Obtener todos los contratos asociados a un empleado específico.
    """
    return contrato_service.get_contratos_by_empleado(db, id_empleado)
