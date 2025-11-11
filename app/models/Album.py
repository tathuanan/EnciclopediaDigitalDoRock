from pydantic import BaseModel

class Album(BaseModel):

    id: int
    titulo: str
    anoLancamento: str
    gravadora: int
    observacoes: str