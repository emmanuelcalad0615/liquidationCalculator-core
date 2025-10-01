from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base  

class TipoContrato(Base):
    __tablename__ = "tipo_contrato"

    id_tipo_contrato = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descripcion = Column(String(255), nullable=False)
    contratos = relationship("Contrato", back_populates="tipo_contrato")


    def __repr__(self):
        return f"<TipoContrato(id={self.id_tipo_contrato}, descripcion='{self.descripcion}')>"
