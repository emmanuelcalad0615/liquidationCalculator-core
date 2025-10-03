from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.tipo_documento import TipoDocumento
from fastapi import HTTPException
from schemas.tipo_documento_schema import TipoDocumentoCreate

def create_tipo_documento(db: Session, tipo_documento: TipoDocumentoCreate):
    try:
        db_tipo_documento = TipoDocumento(
            descripcion=tipo_documento.descripcion
        )
        db.add(db_tipo_documento)
        db.commit()
        db.refresh(db_tipo_documento)
        return db_tipo_documento
    
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail=f"El tipo de documento '{tipo_documento.descripcion}' ya existe"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
#def update_tipo_documento(db:Session, tipo_documento: TipoDocumento)
