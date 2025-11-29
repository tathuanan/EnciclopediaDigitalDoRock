from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.estilo_musical import EstiloMusical


class EstiloMusicalRepository(BaseRepository[EstiloMusical]):
    def __init__(self, db: Session):
        super().__init__(db, EstiloMusical)

    def get_by_nome(self, nome: str) -> List[EstiloMusical]:
        return self.filter_by_ilike(EstiloMusical.nome, nome)  # type: ignore
