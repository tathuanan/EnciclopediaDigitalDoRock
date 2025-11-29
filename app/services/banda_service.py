from typing import List
from sqlalchemy.orm import Session
from app.models.banda import Banda
from app.schemas.banda import BandaCreate, BandaUpdate
from app.repositories.banda_repository import BandaRepository
from app.services.base_service import BaseService


class BandaService(BaseService[Banda, BandaCreate, BandaUpdate]):
    def __init__(self, db: Session):
        super().__init__(BandaRepository(db))
        self.__banda_repository: BandaRepository = self._repository

    def get_by_nome(self, termo: str) -> List[Banda]:
        if len(termo) < 2:
            return []
        return self.__banda_repository.get_by_nome_parcial(termo)
