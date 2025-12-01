from pydantic import BaseModel
from typing import Optional, List


class BandaSimples(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True
        populate_by_name = True


class EstiloMusicalBase(BaseModel):
    nome: str
    descricao: str

    class Config:
        populate_by_name = True


class EstiloMusicalCreate(EstiloMusicalBase):
    pass


class EstiloMusicalUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None

    class Config:
        populate_by_name = True


class EstiloMusical(EstiloMusicalBase):
    id: int
    bandas: List[BandaSimples] = []

    class Config:
        from_attributes = True
        populate_by_name = True
