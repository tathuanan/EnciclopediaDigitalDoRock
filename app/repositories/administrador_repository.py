from typing import Optional
from sqlalchemy.orm import Session
from app.models.administrador import Administrador


class AdministradorRepository:
    def __init__(self, db: Session):
        self.__db = db

    def get_by_email(self, email: str) -> Optional[Administrador]:
        return self.__db.query(Administrador).filter(Administrador.email == email).first()  # type: ignore
