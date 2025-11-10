from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Empleado(Base):
    __tablename__ = "empleado"

    id_empleado = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombres = Column(String(100), nullable=False) 
    apellidos = Column(String(100), nullable=False)
    tipo_documento = Column(Integer, ForeignKey("tipo_documento.id_tipo_documento"), nullable=False)
    documento = Column(String(20), nullable=False, unique=True)
    fecha_nacimiento = Column(Date, nullable=False)
    activo = Column(Boolean, default=True)

    contratos = relationship("Contrato", back_populates="empleado")
    tipo_documento_rel = relationship("TipoDocumento", back_populates="empleados")
    usuario = relationship("User", back_populates="empleado", uselist=False)

    def __repr__(self):
        return f"<Empleado(id={self.id_empleado}, nombre={self.nombres} {self.apellidos})>"
