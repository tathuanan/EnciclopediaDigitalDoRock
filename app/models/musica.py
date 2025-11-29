from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.base import Base


class Musica(Base):
    __tablename__ = "musicas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    duracao_segundos = Column(Integer, nullable=False)
    compositor = Column(String, nullable=True)
    letra_resumo = Column(Text, nullable=True)

    album_id = Column(Integer, ForeignKey("albuns.id"), nullable=False)
    album = relationship("Album", back_populates="musicas")
