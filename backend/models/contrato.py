from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from database import Base  

class Contrato(Base):
    __tablename__ = "contrato"
    id_contrato = Column(Integer, primary_key = True, index = True, autoincrement = True)
    id_empleado = Column(Integer, ForeignKey("empleado.id_empleado"), nullable = False)
    id_tipo_contrato = Column(Integer, ForeignKey("tipo_contrato.id_tipo_contrato"), nullable = False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    salario_mensual = Column(Numeric(10, 2), nullable = False)
    auxilio_transporte = Column(Integer, nullable=True)
    empleado = relationship("Empleado", back_populates="contratos")
    tipo_contrato = relationship("TipoContrato", back_populates="contratos")
    liquidaciones = relationship("Liquidacion", back_populates = "contrato")
    
    def __repr__(self):
        return f"<Contrato(id={self.id_contrato}, empleado={self.id_empleado}, tipo={self.id_tipo_contrato})>"

