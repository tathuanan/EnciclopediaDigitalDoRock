from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.album import Album
from app.models.artista import Artista
from app.schemas.album import AlbumCreate, AlbumUpdate
from app.repositories.album_repository import AlbumRepository
from app.services.base_service import BaseService


class AlbumService(BaseService[Album, AlbumCreate, AlbumUpdate]):
    def __init__(self, db: Session):
        super().__init__(AlbumRepository(db))
        self.__album_repository: AlbumRepository = self._repository
        self.__db = db

    def get_by_banda(self, banda_id: int) -> List[Album]:
        return self.__album_repository.get_by_banda(banda_id)

    def get_by_titulo(self, termo: str) -> List[Album]:
        return self.__album_repository.get_by_titulo_parcial(termo)

    def create(self, obj_in: AlbumCreate) -> Album:
        dados_album = obj_in.model_dump(exclude={"artista_ids"})
        ids_artistas = obj_in.artista_ids

        novo_album = Album(**dados_album)

        if ids_artistas:
            artistas_db = self.__db.query(Artista).filter(Artista.id.in_(ids_artistas)).all()

            novo_album.artistas = artistas_db

        # 4. Salva no banco
        self.__db.add(novo_album)
        self.__db.commit()
        self.__db.refresh(novo_album)

        return novo_album

    def update(self, model_id: int, obj_in: AlbumUpdate) -> Optional[Album]:
        album_db = self.get_by_id(model_id)
        if not album_db:
            return None

        dados_update = obj_in.model_dump(exclude_unset=True)

        if "artista_ids" in dados_update:
            ids = dados_update.pop("artista_ids")

            if ids is not None:
                artistas_db = self.__db.query(Artista).filter(Artista.id.in_(ids)).all()
                album_db.artistas = artistas_db

        return self.__album_repository.update(album_db, dados_update)
