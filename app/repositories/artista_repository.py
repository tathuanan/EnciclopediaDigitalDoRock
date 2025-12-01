from typing import List
from sqlalchemy.orm import Session
from app.models import Banda, Artista
from app.repositories.base_repository import BaseRepository


class ArtistaRepository(BaseRepository[Artista]):
    def __init__(self, db: Session):
        super().__init__(db, Artista)

    def get_by_nome_parcial(self, termo: str) -> List[Artista]:
        return self.filter_by_ilike(Artista.nome, termo)

    def get_by_banda_nome(self, banda: str) -> List[Artista]:
        return self._db.query(Artista).join(Artista.bandas).filter(Banda.nome.ilike(f"%{banda}%")).all()  # type: ignore
