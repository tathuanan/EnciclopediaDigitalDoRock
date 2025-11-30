from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.base import Base


class Instrumento(Base):
    __tablename__ = "instrumentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(Text, nullable=False)

    artistas = relationship("Artista", secondary="instrumento_artista", back_populates="instrumentos")
