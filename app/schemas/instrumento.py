from pydantic import BaseModel
from typing import Optional


class InstrumentoBase(BaseModel):
    nome: str
    descricao: str

    class Config:
        populate_by_name = True


class InstrumentoCreate(InstrumentoBase):
    pass


class InstrumentoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None

    class Config:
        populate_by_name = True


class Instrumento(InstrumentoBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
