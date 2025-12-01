from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models import EstiloMusical, Banda


class EstiloMusicalRepository(BaseRepository[EstiloMusical]):
    def __init__(self, db: Session):
        super().__init__(db, EstiloMusical)

    def get_by_nome(self, nome: str) -> List[EstiloMusical]:
        return self.filter_by_ilike(EstiloMusical.nome, nome)  # type: ignore

    def get_by_banda_nome(self, banda_nome: str) -> List[EstiloMusical]:
        return self._db.query(EstiloMusical).join(EstiloMusical.bandas).filter(Banda.nome.ilike(f"%{banda_nome}%")).all()  # type: ignore
