from typing import List
from sqlalchemy.orm import Session
from app.models.instrumento import Instrumento
from app.schemas.instrumento import InstrumentoCreate, InstrumentoUpdate
from app.repositories.instrumento_repository import InstrumentoRepository
from app.services.base_service import BaseService


class InstrumentoService(BaseService[Instrumento, InstrumentoCreate, InstrumentoUpdate]):
    def __init__(self, db: Session):
        super().__init__(InstrumentoRepository(db))
        self.__instrumento_repository: InstrumentoRepository = self._repository

    def get_by_nome(self, nome: str) -> List[Instrumento]:
        return self.__instrumento_repository.get_by_nome(nome)
