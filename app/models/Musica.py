import string

from pydantic import BaseModel

class Musica(BaseModel):

    id: int
    titulo: str
    duracaoSegundos: int
    compositor: str
    letraResumo: str