from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.base import Base


class Banda(Base):
    __tablename__ = "bandas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    ano_formacao = Column(Integer, nullable=True)
    pais_origem = Column(String, nullable=True)
    em_atividade = Column(Boolean, nullable=True, default=None)
    influencias = Column(String, nullable=True)

    albuns = relationship("Album", back_populates="banda", cascade="all, delete-orphan")
    artistas = relationship("Artista", secondary="banda_artista", back_populates="bandas")

    estilo_musical_id = Column(Integer, ForeignKey("estilos_musicais.id"))
    estilo_musical = relationship("EstiloMusical", back_populates="bandas")