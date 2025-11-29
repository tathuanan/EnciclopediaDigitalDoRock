from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.administrador import LoginRequest, Administrador
from app.services.auth_service import AuthService

router = APIRouter()

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)

@router.post("/login", response_model=Administrador)
def login(login_data: LoginRequest, service: AuthService = Depends(get_auth_service)):
    admin = service.autenticar(login_data.email, login_data.senha)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
        )
    return admin