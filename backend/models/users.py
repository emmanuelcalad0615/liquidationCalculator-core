from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(120), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    id_empleado = Column(Integer, ForeignKey("empleado.id_empleado"), unique=True)
    activo = Column(Boolean, default=True)

    empleado = relationship("Empleado", back_populates="usuario")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
