from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models.contrato import Contrato
from schemas.contrato_schema import ContratoCreate, ContratoUpdate


def create_contrato(db: Session, contrato: ContratoCreate):
    try:
        db_contrato = Contrato(**contrato.dict())
        db.add(db_contrato)
        db.commit()
        db.refresh(db_contrato)
        return db_contrato

    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "Error de integridad en la creación del contrato")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))


def get_all_contratos(db: Session):
    return db.query(Contrato).all()


def get_contrato_by_id(db: Session, id_contrato: int):
    contrato = db.query(Contrato).filter(Contrato.id_contrato == id_contrato).first()
    if not contrato:
        raise HTTPException(404, "Contrato no encontrado")
    return contrato


def update_contrato(db: Session, id_contrato: int, contrato_update: ContratoUpdate):
    contrato = get_contrato_by_id(db, id_contrato)

    for field, value in contrato_update.dict(exclude_unset=True).items():
        setattr(contrato, field, value)

    try:
        db.commit()
        db.refresh(contrato)
        return contrato
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "Error de integridad al actualizar contrato")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))


def delete_contrato(db: Session, id_contrato: int):
    contrato = get_contrato_by_id(db, id_contrato)
    db.delete(contrato)
    db.commit()
    return {"message": "Contrato eliminado correctamente"}
