from pydantic import BaseModel

class EstiloMusical(BaseModel):

    id: int
    nome: str
    descricao: str