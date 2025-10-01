from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.tipo_documento_schema import TipoDocumentoBase, TipoDocumentoCreate, TipoDocumentoOut
import services.tipo_documento_service as tipo_documento_service

router = APIRouter(prefix = "/tipo_documento", tags = ["tipo_documento"])
@router.post("/", response_model = TipoDocumentoOut, status_code = status.HTTP_201_CREATED)
def create_tipo_documento_route(payload: TipoDocumentoCreate, db: Session = Depends(get_db)):
    return tipo_documento_service.create_tipo_documento(db, payload)
