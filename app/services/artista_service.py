from typing import List
from sqlalchemy.orm import Session
from app.models import Instrumento
from app.models.artista import Artista
from app.schemas.artista import ArtistaCreate, ArtistaUpdate
from app.repositories.artista_repository import ArtistaRepository
from app.services.base_service import BaseService


class ArtistaService(BaseService[Artista, ArtistaCreate, ArtistaUpdate]):
    def __init__(self, db: Session):
        super().__init__(ArtistaRepository(db))
        self.__artista_repository: ArtistaRepository = self._repository
        self.__db = db

    def get_by_nome(self, termo: str) -> List[Artista]:
        return self.__artista_repository.get_by_nome_parcial(termo)

    def get_by_banda(self, banda: str) -> List[Artista]:
        return self.__artista_repository.get_by_banda_nome(banda)

    def create(self, obj_in: ArtistaCreate) -> Artista:
        dados_artista = obj_in.model_dump(exclude={"instrumento_ids"})
        ids_instrumentos = obj_in.instrumento_ids

        novo_artista = Artista(**dados_artista)

        if ids_instrumentos:
            instrumentos_db = self.__db.query(Instrumento).filter(Instrumento.id.in_(ids_instrumentos)).all()
            novo_artista.instrumentos = instrumentos_db

        self.__db.add(novo_artista)
        self.__db.commit()
        self.__db.refresh(novo_artista)
        return novo_artista

    def update(self, model_id: int, obj_in: ArtistaUpdate) -> Artista | None:
        artista_db = self.get_by_id(model_id)
        if not artista_db:
            return None

        dados_update = obj_in.model_dump(exclude_unset=True)

        if "instrumento_ids" in dados_update:
            ids = dados_update.pop("instrumento_ids")
            if ids is not None:
                instrumentos_db = self.__db.query(Instrumento).filter(Instrumento.id.in_(ids)).all()
                artista_db.instrumentos = instrumentos_db

        return self.__artista_repository.update(artista_db, dados_update)
