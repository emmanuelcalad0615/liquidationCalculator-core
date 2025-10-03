from sqlalchemy.orm import Session
from models.empleado import Empleado
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from schemas.empleado_schema import EmpleadoCreate, EmpleadoUpdate
from services.utils import handle_integrity_error

def create_empleado(db:Session, empleado: EmpleadoCreate):
    try:
        db_empleado = Empleado( 
            nombres = empleado.nombres,
            apellidos = empleado.apellidos,
            tipo_documento = empleado.tipo_documento,
            documento = empleado.documento,
            fecha_nacimiento = empleado.fecha_nacimiento
        )
        db.add(db_empleado)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado
    except IntegrityError:
       db.rollback()
       raise HTTPException(status_code=409, detail="El empleado ya existe con ese documento o email")
    
def update_empleado(db: Session, empleado_id: int, empleado_data: EmpleadoUpdate):
    empleado = db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()
    if not empleado:
        raise HTTPException(
            status_code=404,
            detail={"error": "Empleado no encontrado", "code": 404}
        )

    try:
        update_data = empleado_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(empleado, key, value)

        db.commit()
        db.refresh(empleado)
        return empleado

    except IntegrityError as e:
        db.rollback()
        raise handle_integrity_error(e, entity="Empleado")
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail={"error": f"Error al actualizar empleado: {str(e)}", "code": 500}
        )

def get_empleados_by_id(db: Session, empleado_id: int) -> Empleado:
    empleado = db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

def get_empleados_all(db:Session) -> list[Empleado]:
    return db.query(Empleado).all()
