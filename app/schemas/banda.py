from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.estilo_musical import EstiloMusical


class AlbumSimples(BaseModel):
    id: int
    titulo: str
    ano_lancamento: Optional[int] = Field(None, alias="anoLancamento")

    class Config:
        from_attributes = True
        populate_by_name = True


class BandaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    ano_formacao: Optional[int] = Field(None, alias="anoFormacao")
    pais_origem: Optional[str] = Field(None, alias="paisOrigem")
    em_atividade: bool = Field(True, alias="emAtividade")
    influencias: Optional[str] = Field(None, alias="influenciasTexto")

    class Config:
        populate_by_name = True


class BandaCreate(BandaBase):
    estilo_musical_id: Optional[int] = Field(None, alias="estiloMusicalId")


class BandaUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    ano_formacao: Optional[int] = Field(None, alias="anoFormacao")
    pais_origem: Optional[str] = Field(None, alias="paisOrigem")
    em_atividade: Optional[bool] = Field(None, alias="emAtividade")
    influencias: Optional[str] = Field(None, alias="influenciasTexto")
    estilo_musical_id: Optional[int] = Field(None, alias="estiloMusicalId")

    class Config:
        populate_by_name = True


class Banda(BandaBase):
    id: int
    estilo_musical: Optional[EstiloMusical] = Field(None, alias="estiloMusical")
    albuns: List[AlbumSimples] = Field(default=[], alias="albums")

    class Config:
        from_attributes = True
        populate_by_name = True
