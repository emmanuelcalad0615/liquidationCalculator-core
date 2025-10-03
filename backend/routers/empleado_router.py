from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.empleado_schema import EmpleadoCreate, EmpleadoOut, EmpleadoUpdate, EmpleadoBase
import services.empleado_service as empleado_service

router = APIRouter(prefix = "/empleados", tags = ["empleados"])

@router.post("/", response_model = EmpleadoOut, status_code = status.HTTP_201_CREATED)
def create_empleado_route(payload: EmpleadoCreate, db: Session = Depends(get_db)):
    return empleado_service.create_empleado(db, payload)

@router.put("/{id_empleado}", response_model = EmpleadoOut, status_code = status.HTTP_200_OK)
def update_empleado_route(id_empleado: int, payload: EmpleadoUpdate, db: Session = Depends(get_db)):
    return empleado_service.update_empleado(db, id_empleado, payload)

@router.get("/{id_empleado}", response_model = EmpleadoOut, status_code = status.HTTP_200_OK)
def get_empleados_id(id_empleado: int, db: Session = Depends(get_db)):
    return empleado_service.get_empleados_by_id(db, id_empleado)

@router.get("/", response_model = list[EmpleadoOut], status_code = status.HTTP_200_OK)
def get_empleados_all(db: Session = Depends(get_db)):
    return empleado_service.get_empleados_all(db)


