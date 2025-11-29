from pydantic import BaseModel


class AdministradorBase(BaseModel):
    nome: str
    email: str
    ativo: bool

    class Config:
        populate_by_name = True


class Administrador(AdministradorBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True


class LoginRequest(BaseModel):
    email: str
    senha: str
