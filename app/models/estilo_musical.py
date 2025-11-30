from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.base import Base


class EstiloMusical(Base):
    __tablename__ = "estilos_musicais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(Text, nullable=False)

    bandas = relationship("Banda", back_populates="estilo_musical")
