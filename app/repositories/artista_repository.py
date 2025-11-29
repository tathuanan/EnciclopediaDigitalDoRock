from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.artista import Artista


class ArtistaRepository(BaseRepository[Artista]):
    def __init__(self, db: Session):
        super().__init__(db, Artista)

    def get_by_nome_parcial(self, termo: str) -> List[Artista]:
        return self.filter_by_ilike(Artista.nome, termo)
