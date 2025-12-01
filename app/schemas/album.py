from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.musica import Musica


class ArtistaSimples(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


class AlbumBase(BaseModel):
    titulo: str
    ano_lancamento: Optional[int] = Field(None, alias="anoLancamento")
    gravadora: Optional[str] = None
    observacoes: Optional[str] = None

    class Config:
        populate_by_name = True


class AlbumCreate(AlbumBase):
    banda_id: int = Field(..., alias="bandaId")
    artista_ids: List[int] = Field(default=[], alias="artistaIds")


class AlbumUpdate(BaseModel):
    titulo: Optional[str] = None
    ano_lancamento: Optional[int] = Field(None, alias="anoLancamento")
    gravadora: Optional[str] = None
    observacoes: Optional[str] = None
    banda_id: Optional[int] = Field(None, alias="bandaId")
    artista_ids: Optional[List[int]] = Field(None, alias="artistaIds")

    class Config:
        populate_by_name = True


class Album(AlbumBase):
    id: int
    banda_id: Optional[int] = Field(None, alias="bandaId")
    musicas: List[Musica] = []
    artistas: List[ArtistaSimples] = []

    class Config:
        from_attributes = True
        populate_by_name = True
