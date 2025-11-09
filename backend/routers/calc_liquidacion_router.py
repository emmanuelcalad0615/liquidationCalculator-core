from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.calc_liquidacion_service import LiquidacionCalculator
from schemas.calc_liquidacion_schemas import LiquidacionRequest, LiquidacionResponse

router = APIRouter(prefix="/calc_liquidaciones", tags=["CalcLiquidaciones"])


@router.post("/calcular", response_model=LiquidacionResponse)
def calcular_liquidacion(data: LiquidacionRequest, db: Session = Depends(get_db)):
    try:
        servicio = LiquidacionCalculator(db)
        resultado = servicio.calcular(data.id_contrato, data.id_motivo_terminacion)
        return resultado
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
