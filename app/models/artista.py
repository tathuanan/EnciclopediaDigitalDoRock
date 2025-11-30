from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from app.core.base import Base


class Artista(Base):
    __tablename__ = "artistas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(DateTime, nullable=False)
    pais_origem = Column(String, nullable=False)
    bio = Column(Text, nullable=False)

    instrumentos = relationship("Instrumento", secondary="instrumento_artista", back_populates="artistas")
    bandas = relationship("Banda", secondary="banda_artista", back_populates="artistas")
    albuns = relationship("Album", secondary="album_artista", back_populates="artistas")
