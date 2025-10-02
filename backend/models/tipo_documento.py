from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from database import Base

class TipoDocumento(Base):
    __tablename__ = "tipo_documento"
    id_tipo_documento = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descripcion = Column(String(255), nullable=False )
    empleados = relationship("Empleado", back_populates="tipo_documento_rel")

    def __repr__(self):
        return f"TipoDocumento(id: {self.id_tipo_documento}, tipo: '{self.descripcion}')"
