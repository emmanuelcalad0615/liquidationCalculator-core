from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.tipo_documento_schema import TipoDocumentoCreate, TipoDocumentoOut, TipoDocumentoUpdate
import services.tipo_documento_service as tipo_documento_service

router = APIRouter(prefix="/tipo_documento", tags=["TipoDocumento"])

@router.post("/", response_model=TipoDocumentoOut, status_code=status.HTTP_201_CREATED)
def create_tipo_documento_route(payload: TipoDocumentoCreate, db: Session = Depends(get_db)):
    return tipo_documento_service.create_tipo_documento(db, payload)

@router.get("/", response_model=list[TipoDocumentoOut])
def get_all_tipo_documentos_route(db: Session = Depends(get_db)):
    return tipo_documento_service.get_all_tipo_documentos(db)

@router.get("/{id_tipo_documento}", response_model=TipoDocumentoOut)
def get_tipo_documento_by_id_route(id_tipo_documento: int, db: Session = Depends(get_db)):
    return tipo_documento_service.get_tipo_documento_by_id(db, id_tipo_documento)

@router.put("/{id_tipo_documento}", response_model=TipoDocumentoOut)
def update_tipo_documento_route(id_tipo_documento: int, payload: TipoDocumentoUpdate, db: Session = Depends(get_db)):
    return tipo_documento_service.update_tipo_documento(db, id_tipo_documento, payload)

@router.delete("/{id_tipo_documento}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tipo_documento_route(id_tipo_documento: int, db: Session = Depends(get_db)):
    return tipo_documento_service.delete_tipo_documento(db, id_tipo_documento)
