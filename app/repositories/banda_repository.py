from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.banda import Banda


class BandaRepository(BaseRepository[Banda]):
    def __init__(self, db: Session):
        super().__init__(db, Banda)

    def get_by_nome_parcial(self, termo: str) -> List[Banda]:
        return self.filter_by_ilike(Banda.nome, termo)

    def get_by_estilo(self, estilo_id: int) -> List[Banda]:
        return self._db.query(Banda).filter(Banda.estilo_musical_id == estilo_id).all()  # type: ignore
