from typing import List
from sqlalchemy.orm import Session
from app.models.estilo_musical import EstiloMusical
from app.schemas.estilo_musical import EstiloMusicalCreate, EstiloMusicalUpdate
from app.repositories.estilo_musical_repository import EstiloMusicalRepository
from app.services.base_service import BaseService


class EstiloMusicalService(BaseService[EstiloMusical, EstiloMusicalCreate, EstiloMusicalUpdate]):
    def __init__(self, db: Session):
        super().__init__(EstiloMusicalRepository(db))
        self.__estilo_repository: EstiloMusicalRepository = self._repository

    def get_by_nome(self, nome: str) -> List[EstiloMusical]:
        return self.__estilo_repository.get_by_nome(nome)
