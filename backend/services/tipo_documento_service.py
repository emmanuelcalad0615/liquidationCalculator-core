from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.tipo_documento import TipoDocumento
from fastapi import HTTPException
from schemas.tipo_documento_schema import TipoDocumentoCreate, TipoDocumentoUpdate

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
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail=f"El tipo de documento '{tipo_documento.descripcion}' ya existe"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_all_tipo_documentos(db: Session):
    return db.query(TipoDocumento).all()


def get_tipo_documento_by_id(db: Session, id_tipo_documento: int):
    tipo_doc = db.query(TipoDocumento).filter(TipoDocumento.id_tipo_documento == id_tipo_documento).first()
    if not tipo_doc:
        raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")
    return tipo_doc


def update_tipo_documento(db: Session, id_tipo_documento: int, tipo_documento_update: TipoDocumentoUpdate):
    tipo_doc = get_tipo_documento_by_id(db, id_tipo_documento)

    if tipo_documento_update.descripcion is not None:
        tipo_doc.descripcion = tipo_documento_update.descripcion

    try:
        db.commit()
        db.refresh(tipo_doc)
        return tipo_doc
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail=f"El tipo de documento '{tipo_documento_update.descripcion}' ya existe"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def delete_tipo_documento(db: Session, id_tipo_documento: int):
    tipo_doc = get_tipo_documento_by_id(db, id_tipo_documento)
    db.delete(tipo_doc)
    db.commit()
    return {"message": "Tipo de documento eliminado correctamente"}
