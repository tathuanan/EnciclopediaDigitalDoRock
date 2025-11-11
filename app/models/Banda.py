from pydantic import BaseModel

from app.models.Album import Album


class Banda(BaseModel):

    id: int
    nome: str
    descricao: str
    anoFormacao: int
    paisOrigem: str
    emAtividade: bool
    influcenciasTexto: str
    albums: list[Album]