from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Liquidacion(Base):
    __tablename__ = "liquidacion"

    id_liquidacion = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_contrato = Column(Integer, ForeignKey("contrato.id_contrato"), nullable=False)
    fecha_liquidacion = Column(Date, nullable=False)
    id_motivo_terminacion = Column(Integer, ForeignKey("motivo_terminacion.id_motivo_terminacion"), nullable=False)
    total_liquidacion = Column(Numeric(12, 2), nullable=False)

    # Relaciones
    contrato = relationship("Contrato", back_populates="liquidaciones")
    motivo_terminacion = relationship("MotivoTerminacion", back_populates="liquidaciones")
    detalles_liquidacion = relationship(
        "DetalleLiquidacion",
        back_populates="liquidacion",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<Liquidacion(id={self.id_liquidacion}, contrato={self.id_contrato}, "
            f"motivo_terminacion={self.id_motivo_terminacion}, total={self.total_liquidacion})>"
        )
