from typing import List
from sqlalchemy.orm import Session
from app.models import EstiloMusical, Artista
from app.repositories.base_repository import BaseRepository
from app.models.banda import Banda


class BandaRepository(BaseRepository[Banda]):
    def __init__(self, db: Session):
        super().__init__(db, Banda)

    def get_by_nome_parcial(self, termo: str) -> List[Banda]:
        return self.filter_by_ilike(Banda.nome, termo)

    def get_by_estilo(self, estilo_nome: str) -> List[Banda]:
        return self._db.query(Banda).join(Banda.estilo_musical).filter(EstiloMusical.nome.ilike(f"%{estilo_nome}%")).all() # type: ignore

    def get_by_artista(self, artista_nome: str) -> List[Banda]:
        return self._db.query(Banda).join(Banda.artistas).filter(Artista.nome.ilike(f"%{artista_nome}%")).all()  # type: ignore
