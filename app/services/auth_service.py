from typing import Optional
from sqlalchemy.orm import Session
from app.models.administrador import Administrador
from app.repositories.administrador_repository import AdministradorRepository
from app.core.security import verifica_senha


class AuthService:
    def __init__(self, db: Session):
        self.__admin_repository = AdministradorRepository(db)

    def autenticar(self, email: str, senha: str) -> Optional[Administrador]:
        admin = self.__admin_repository.get_by_email(email)
        if not admin:
            return None
        if not verifica_senha(senha, admin.senha_hash):
            return None
        if not admin.ativo:
            return None
        return admin
