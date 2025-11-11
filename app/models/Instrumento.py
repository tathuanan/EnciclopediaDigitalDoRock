from pydantic import BaseModel

class Instrumento(BaseModel):

    id: int
    nome: str
    descricao: str