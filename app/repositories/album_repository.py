from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.album import Album


class AlbumRepository(BaseRepository[Album]):
    def __init__(self, db: Session):
        super().__init__(db, Album)

    def get_by_banda(self, banda_id: int) -> List[Album]:
        return self._db.query(Album).filter(Album.banda_id == banda_id).all()  # type: ignore

    def get_by_titulo_parcial(self, termo: str) -> List[Album]:
        return self.filter_by_ilike(Album.titulo, termo)
