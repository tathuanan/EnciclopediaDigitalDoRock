from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.base import Base

banda_artista_table = Table(
    "banda_artista",
    Base.metadata,
    Column("banda_id", Integer, ForeignKey("bandas.id"), primary_key=True),
    Column("artista_id", Integer, ForeignKey("artistas.id"), primary_key=True)
)

album_artista_table = Table(
    "album_artista",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albuns.id"), primary_key=True),
    Column("artista_id", Integer, ForeignKey("artistas.id"), primary_key=True)
)

instrumento_artista_table = Table(
    "instrumento_artista",
    Base.metadata,
    Column("instrumento_id", Integer, ForeignKey("instrumentos.id"), primary_key=True),
    Column("artista_id", Integer, ForeignKey("artistas.id"), primary_key=True)
)
