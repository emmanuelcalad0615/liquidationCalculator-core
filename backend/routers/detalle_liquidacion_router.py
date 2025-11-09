from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.detalle_liquidacion_schema import (
    DetalleLiquidacionCreate,
    DetalleLiquidacionUpdate,
    DetalleLiquidacionOut,
)
import services.detalle_liquidacion_service as detalle_service


router = APIRouter(prefix="/detalle_liquidacion", tags=["DetalleLiquidacion"])


@router.post("/", response_model=DetalleLiquidacionOut, status_code=status.HTTP_201_CREATED)
def create_detalle_route(payload: DetalleLiquidacionCreate, db: Session = Depends(get_db)):
    return detalle_service.create_detalle_liquidacion(db, payload)


@router.get("/", response_model=list[DetalleLiquidacionOut])
def get_all_detalles_route(db: Session = Depends(get_db)):
    return detalle_service.get_all_detalles(db)


@router.get("/{id_detalle}", response_model=DetalleLiquidacionOut)
def get_detalle_by_id_route(id_detalle: int, db: Session = Depends(get_db)):
    return detalle_service.get_detalle_by_id(db, id_detalle)


@router.put("/{id_detalle}", response_model=DetalleLiquidacionOut)
def update_detalle_route(id_detalle: int, payload: DetalleLiquidacionUpdate, db: Session = Depends(get_db)):
    return detalle_service.update_detalle_liquidacion(db, id_detalle, payload)


@router.delete("/{id_detalle}", status_code=status.HTTP_204_NO_CONTENT)
def delete_detalle_route(id_detalle: int, db: Session = Depends(get_db)):
    detalle_service.delete_detalle_liquidacion(db, id_detalle)
