from typing import List
from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from app.models.musica import Musica


class MusicaRepository(BaseRepository[Musica]):
    def __init__(self, db: Session):
        super().__init__(db, Musica)

    def get_by_titulo_parcial(self, termo: str) -> List[Musica]:
        return self.filter_by_ilike(Musica.titulo, termo)

    def get_by_album(self, album_id: int) -> List[Musica]:
        return self._db.query(Musica).filter(Musica.album_id == album_id).all()  # type: ignore
