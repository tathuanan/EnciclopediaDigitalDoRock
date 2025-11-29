from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.schemas.instrumento import Instrumento


class BandaSimples(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


class AlbumSimples(BaseModel):
    id: int
    titulo: str

    class Config:
        from_attributes = True


class ArtistaBase(BaseModel):
    nome: str
    data_nascimento: datetime = Field(..., alias="dataNascimento")
    pais_origem: str = Field(..., alias="paisOrigem")
    bio: str

    class Config:
        populate_by_name = True


class ArtistaCreate(ArtistaBase):
    instrumento_ids: List[int] = []


class ArtistaUpdate(BaseModel):
    nome: Optional[str] = None
    data_nascimento: Optional[datetime] = Field(None, alias="dataNascimento")
    pais_origem: Optional[str] = Field(None, alias="paisOrigem")
    bio: Optional[str] = None
    instrumento_ids: Optional[List[int]] = None

    class Config:
        populate_by_name = True


class Artista(ArtistaBase):
    id: int
    instrumentos: List[Instrumento] = []
    bandas: List[BandaSimples] = []
    albums: List[AlbumSimples] = Field(default=[], alias="albums")

    class Config:
        from_attributes = True
        populate_by_name = True
