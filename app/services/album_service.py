from typing import List
from sqlalchemy.orm import Session
from app.models.album import Album
from app.schemas.album import AlbumCreate, AlbumUpdate
from app.repositories.album_repository import AlbumRepository
from app.services.base_service import BaseService


class AlbumService(BaseService[Album, AlbumCreate, AlbumUpdate]):
    def __init__(self, db: Session):
        super().__init__(AlbumRepository(db))
        self.__album_repository: AlbumRepository = self._repository

    def get_by_banda(self, banda_id: int) -> List[Album]:
        return self.__album_repository.get_by_banda(banda_id)

    def get_by_titulo(self, termo: str) -> List[Album]:
        return self.__album_repository.get_by_titulo_parcial(termo)
