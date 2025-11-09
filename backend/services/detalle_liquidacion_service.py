from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from models.detalle_liquidacion import DetalleLiquidacion
from schemas.detalle_liquidacion_schema import DetalleLiquidacionCreate, DetalleLiquidacionUpdate


def create_detalle_liquidacion(db: Session, detalle: DetalleLiquidacionCreate):
    try:
        db_detalle = DetalleLiquidacion(
            id_liquidacion=detalle.id_liquidacion,
            concepto=detalle.concepto,
            valor=detalle.valor
        )
        db.add(db_detalle)
        db.commit()
        db.refresh(db_detalle)
        return db_detalle

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Error de integridad: id_liquidacion no válido o concepto duplicado."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_all_detalles(db: Session):
    return db.query(DetalleLiquidacion).all()


def get_detalle_by_id(db: Session, id_detalle: int):
    detalle = db.query(DetalleLiquidacion).filter(
        DetalleLiquidacion.id_detalle == id_detalle
    ).first()

    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de liquidación no encontrado")

    return detalle


def update_detalle_liquidacion(db: Session, id_detalle: int, update_data: DetalleLiquidacionUpdate):
    try:
        detalle_db = get_detalle_by_id(db, id_detalle)

        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(detalle_db, key, value)

        db.commit()
        db.refresh(detalle_db)
        return detalle_db

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad al actualizar detalle")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def delete_detalle_liquidacion(db: Session, id_detalle: int):
    try:
        detalle_db = get_detalle_by_id(db, id_detalle)
        db.delete(detalle_db)
        db.commit()
        return {"message": "Detalle eliminado correctamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
