from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class MotivoTerminacion(Base):
    __tablename__ = "motivo_terminacion"
    id_motivo_terminacion = Column(Integer, primary_key = True, index = True, autoincrement = True)
    descripcion = Column(String(255), nullable=False)
    liquidaciones = relationship("Liquidacion", back_populates = "motivo_terminacion")

    def __repr__(self):
        return f"<MotivoLiquidacion(id={self.id_motivo_terminacion}, descripcion='{self.descripcion}')>"