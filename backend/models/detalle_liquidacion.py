from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DetalleLiquidacion(Base):
    __tablename__ = "detalle_liquidacion"

    id_detalle = Column(Integer, primary_key = True, index = True, autoincrement = True)
    id_liquidacion = Column(Integer, ForeignKey("liquidacion.id_liquidacion"), nullable = False)
    concepto = Column(String(255), nullable = False )
    valor = Column(Numeric(30, 2), nullable = False)
    liquidacion = relationship("Liquidacion", back_populates = "detalles_liquidacion")

    def __repr__(self):
        return f"<DetalleLiquidacion(id = {self.id_detalle}, concepto = '{self.concepto}', valor = {self.valor})>"

