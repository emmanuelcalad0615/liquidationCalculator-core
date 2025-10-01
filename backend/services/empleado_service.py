from sqlalchemy.orm import Session
from models.empleado import Empleado
from schemas.empleado_schema import EmpleadoCreate

def create_empleado(db:Session, empleado: EmpleadoCreate):
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