from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from models.motivo_terminacion import MotivoTerminacion
from schemas.motivo_terminacion_schema import MotivoTerminacionCreate, MotivoTerminacionUpdate


def create_motivo_terminacion(db: Session, motivo: MotivoTerminacionCreate):
    try:
        db_motivo = MotivoTerminacion(descripcion=motivo.descripcion)
        db.add(db_motivo)
        db.commit()
        db.refresh(db_motivo)
        return db_motivo

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail=f"El motivo de terminación '{motivo.descripcion}' ya existe"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_all_motivos(db: Session):
    return db.query(MotivoTerminacion).all()


def get_motivo_by_id(db: Session, id_motivo_terminacion: int):
    motivo = db.query(MotivoTerminacion).filter(
        MotivoTerminacion.id_motivo_terminacion == id_motivo_terminacion
    ).first()

    if not motivo:
        raise HTTPException(status_code=404, detail="Motivo de terminación no encontrado")

    return motivo


def update_motivo_terminacion(db: Session, id_motivo_terminacion: int, motivo_update: MotivoTerminacionUpdate):
    try:
        motivo_db = get_motivo_by_id(db, id_motivo_terminacion)

        for key, value in motivo_update.dict(exclude_unset=True).items():
            setattr(motivo_db, key, value)

        db.commit()
        db.refresh(motivo_db)
        return motivo_db

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="El motivo actualizado ya existe")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def delete_motivo_terminacion(db: Session, id_motivo_terminacion: int):
    try:
        motivo_db = get_motivo_by_id(db, id_motivo_terminacion)
        db.delete(motivo_db)
        db.commit()
        return {"message": "Motivo de terminación eliminado correctamente"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
