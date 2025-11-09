from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db

from schemas.liquidacion_schema import LiquidacionCreate, LiquidacionOut, LiquidacionUpdate
import services.liquidacion_service as liquidacion_service

router = APIRouter(prefix="/liquidacion", tags=["Liquidación"])

@router.post("/", response_model=LiquidacionOut, status_code=status.HTTP_201_CREATED)
def create_liquidacion_route(payload: LiquidacionCreate, db: Session = Depends(get_db)):
    return liquidacion_service.create_liquidacion(db, payload)


@router.get("/", response_model=list[LiquidacionOut])
def get_all_liquidaciones_route(db: Session = Depends(get_db)):
    return liquidacion_service.get_all_liquidaciones(db)


@router.get("/{id_liquidacion}", response_model=LiquidacionOut)
def get_liquidacion_by_id_route(id_liquidacion: int, db: Session = Depends(get_db)):
    return liquidacion_service.get_liquidacion_by_id(db, id_liquidacion)


@router.put("/{id_liquidacion}", response_model=LiquidacionOut)
def update_liquidacion_route(id_liquidacion: int, payload: LiquidacionUpdate, db: Session = Depends(get_db)):
    return liquidacion_service.update_liquidacion(db, id_liquidacion, payload)


@router.delete("/{id_liquidacion}", status_code=status.HTTP_204_NO_CONTENT)
def delete_liquidacion_route(id_liquidacion: int, db: Session = Depends(get_db)):
    liquidacion_service.delete_liquidacion(db, id_liquidacion)
