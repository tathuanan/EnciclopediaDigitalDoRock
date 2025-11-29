from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.base import Base


class Album(Base):
    __tablename__ = "albuns"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    ano_lancamento = Column(Integer, nullable=True)
    gravadora = Column(String, nullable=True)
    observacoes = Column(String, nullable=True)

    musicas = relationship("Musica", back_populates="album", cascade="all, delete-orphan")
    artistas = relationship("Artista", secondary="album_artista", back_populates="albuns")

    banda_id = Column(Integer, ForeignKey("bandas.id"))
    banda = relationship("Banda", back_populates="albuns")
