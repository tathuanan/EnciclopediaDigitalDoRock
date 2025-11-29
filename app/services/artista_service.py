from typing import List
from sqlalchemy.orm import Session
from app.models.artista import Artista
from app.schemas.artista import ArtistaCreate, ArtistaUpdate
from app.repositories.artista_repository import ArtistaRepository
from app.services.base_service import BaseService


class ArtistaService(BaseService[Artista, ArtistaCreate, ArtistaUpdate]):
    def __init__(self, db: Session):
        super().__init__(ArtistaRepository(db))
        self.__artista_repository: ArtistaRepository = self._repository

    def create(self, obj_in: ArtistaCreate) -> Artista:
        return super().create(obj_in)

    def get_by_nome(self, termo: str) -> List[Artista]:
        return self.__artista_repository.get_by_nome_parcial(termo)
