from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models.liquidacion import Liquidacion
from schemas.liquidacion_schema import LiquidacionCreate, LiquidacionUpdate


def create_liquidacion(db: Session, liquidacion: LiquidacionCreate):
    try:
        db_liquidacion = Liquidacion(
            id_contrato=liquidacion.id_contrato,
            fecha_liquidacion=liquidacion.fecha_liquidacion,
            id_motivo_terminacion=liquidacion.id_motivo_terminacion,
            total_liquidacion=liquidacion.total_liquidacion
        )

        db.add(db_liquidacion)
        db.commit()
        db.refresh(db_liquidacion)

# 🔹 Traer la liquidación con relaciones completas
        liquidacion_full = (
            db.query(Liquidacion)
            .options(
                joinedload(Liquidacion.motivo_terminacion),
                joinedload(Liquidacion.detalles_liquidacion)
            )
            .filter(Liquidacion.id_liquidacion == db_liquidacion.id_liquidacion)
            .first()
        )

        return liquidacion_full


    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Error al crear liquidación (validación o FK no válida)"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_all_liquidaciones(db: Session):
    return (
        db.query(Liquidacion)
        .options(
            joinedload(Liquidacion.motivo_terminacion),
            joinedload(Liquidacion.detalles_liquidacion)
        )
        .all()
    )


def get_liquidacion_by_id(db: Session, id_liquidacion: int):
    liquidacion = (
        db.query(Liquidacion)
        .options(
            joinedload(Liquidacion.motivo_terminacion),
            joinedload(Liquidacion.detalles_liquidacion)
        )
        .filter(Liquidacion.id_liquidacion == id_liquidacion)
        .first()
    )

    if not liquidacion:
        raise HTTPException(status_code=404, detail="Liquidación no encontrada")

    return liquidacion


def update_liquidacion(db: Session, id_liquidacion: int, liquidacion_update: LiquidacionUpdate):
    try:
        liquidacion_db = get_liquidacion_by_id(db, id_liquidacion)

        for key, value in liquidacion_update.dict(exclude_unset=True).items():
            setattr(liquidacion_db, key, value)

        db.commit()
        db.refresh(liquidacion_db)
        return liquidacion_db

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Error al actualizar liquidación (validación o FK no válida)"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def delete_liquidacion(db: Session, id_liquidacion: int):
    try:
        liquidacion_db = get_liquidacion_by_id(db, id_liquidacion)
        db.delete(liquidacion_db)
        db.commit()
        return {"message": "Liquidación eliminada correctamente"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
