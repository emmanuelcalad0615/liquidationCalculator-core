from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models.tipo_contrato import TipoContrato
from schemas.tipo_contrato_schema import TipoContratoCreate, TipoContratoUpdate

def create_tipo_contrato(db: Session, tipo_contrato: TipoContratoCreate):
    try:
        db_tipo = TipoContrato(descripcion=tipo_contrato.descripcion)
        db.add(db_tipo)
        db.commit()
        db.refresh(db_tipo)
        return db_tipo
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail=f"El tipo de contrato '{tipo_contrato.descripcion}' ya existe"
        )


def get_all_tipo_contratos(db: Session):
    return db.query(TipoContrato).all()


def get_tipo_contrato_by_id(db: Session, id_tipo_contrato: int):
    tipo = db.query(TipoContrato).filter(TipoContrato.id_tipo_contrato == id_tipo_contrato).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de contrato no encontrado")
    return tipo


def update_tipo_contrato(db: Session, id_tipo_contrato: int, tipo_update: TipoContratoUpdate):
    tipo_db = get_tipo_contrato_by_id(db, id_tipo_contrato)

    for key, value in tipo_update.dict(exclude_unset=True).items():
        setattr(tipo_db, key, value)

    db.commit()
    db.refresh(tipo_db)
    return tipo_db


def delete_tipo_contrato(db: Session, id_tipo_contrato: int):
    tipo_db = get_tipo_contrato_by_id(db, id_tipo_contrato)
    db.delete(tipo_db)
    db.commit()
    return {"message": "Tipo de contrato eliminado correctamente"}
