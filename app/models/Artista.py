from datetime import datetime
from pydantic import BaseModel

from app.models.Instrumento import Instrumento


class Artista(BaseModel):

    id: int
    nome: str
    dataNascimento: datetime
    paisOrigem: str
    bio: str
    instrumentos: list[Instrumento]