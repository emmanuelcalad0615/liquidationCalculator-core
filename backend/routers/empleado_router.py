from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.empleado_schema import EmpleadoCreate, EmpleadoOut, EmpleadoUpdate
import services.empleado_service as empleado_service

router = APIRouter(prefix = "/empleados", tags = ["empleados"])
@router.post("/", response_model = EmpleadoOut, status_code = status.HTTP_201_CREATED)
def create_empleado_route(payload: EmpleadoCreate, db: Session = Depends(get_db)):
    return empleado_service.create_empleado(db, payload)