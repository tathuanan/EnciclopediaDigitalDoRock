from pydantic import BaseModel, Field
from typing import Optional


class MusicaBase(BaseModel):
    titulo: str
    duracao_segundos: int = Field(..., alias="duracaoSegundos", gt=0)
    compositor: Optional[str] = None
    letra_resumo: Optional[str] = Field(None, alias="letraResumo")

    class Config:
        populate_by_name = True


class MusicaCreate(MusicaBase):
    album_id: int = Field(..., alias="albumId")


class MusicaUpdate(BaseModel):
    titulo: Optional[str] = None
    duracao_segundos: Optional[int] = Field(None, alias="duracaoSegundos")
    compositor: Optional[str] = None
    letra_resumo: Optional[str] = Field(None, alias="letraResumo")
    album_id: Optional[int] = Field(None, alias="albumId")

    class Config:
        populate_by_name = True


class Musica(MusicaBase):
    id: int
    album_id: int = Field(..., alias="albumId")

    class Config:
        from_attributes = True
        populate_by_name = True
