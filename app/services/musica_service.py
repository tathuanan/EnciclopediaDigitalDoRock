from typing import List
from sqlalchemy.orm import Session
from app.models.musica import Musica
from app.schemas.musica import MusicaCreate, MusicaUpdate
from app.repositories.musica_repository import MusicaRepository
from app.services.base_service import BaseService


class MusicaService(BaseService[Musica, MusicaCreate, MusicaUpdate]):
    def __init__(self, db: Session):
        super().__init__(MusicaRepository(db))
        self.__musica_repository: MusicaRepository = self._repository

    def get_by_titulo(self, termo: str) -> List[Musica]:
        return self.__musica_repository.get_by_titulo_parcial(termo)

    def get_by_album(self, album_id: int) -> List[Musica]:
        return self.__musica_repository.get_by_album(album_id)
