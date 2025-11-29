from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.instrumento import Instrumento


class InstrumentoRepository(BaseRepository[Instrumento]):
    def __init__(self, db: Session):
        super().__init__(db, Instrumento)

    def get_by_nome(self, nome: str) -> List[Instrumento]:
        return self.filter_by_ilike(Instrumento.nome, nome)
