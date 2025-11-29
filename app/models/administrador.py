from sqlalchemy import Column, Integer, String, Boolean
from app.core.base import Base


class Administrador(Base):
    __tablename__ = "administrador"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
