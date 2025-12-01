from typing import List
from sqlalchemy.orm import Session
from app.models.banda import Banda
from app.models.artista import Artista
from app.schemas.banda import BandaCreate, BandaUpdate
from app.repositories.banda_repository import BandaRepository
from app.services.base_service import BaseService


class BandaService(BaseService[Banda, BandaCreate, BandaUpdate]):
    def __init__(self, db: Session):
        super().__init__(BandaRepository(db))
        self.__banda_repository: BandaRepository = self._repository
        self.__db = db

    def get_by_nome(self, termo: str) -> List[Banda]:
        if len(termo) < 2:
            return []
        return self.__banda_repository.get_by_nome_parcial(termo)

    def create(self, obj_in: BandaCreate) -> Banda:
        dados_banda = obj_in.model_dump(exclude={"artista_ids"})
        ids_artistas = obj_in.artista_ids

        nova_banda = Banda(**dados_banda)

        if ids_artistas:
            artistas_db = self.__db.query(Artista).filter(Artista.id.in_(ids_artistas)).all()
            nova_banda.artistas = artistas_db

        self.__db.add(nova_banda)
        self.__db.commit()
        self.__db.refresh(nova_banda)
        return nova_banda

    def update(self, model_id: int, obj_in: BandaUpdate) -> Banda | None:
        banda_db = self.get_by_id(model_id)
        if not banda_db:
            return None

        dados_update = obj_in.model_dump(exclude_unset=True)

        if "artista_ids" in dados_update:
            ids = dados_update.pop("artista_ids")
            if ids is not None:
                artistas_db = self.__db.query(Artista).filter(Artista.id.in_(ids)).all()
                banda_db.artistas = artistas_db

        return self._repository.update(banda_db, dados_update)
