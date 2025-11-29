import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.administrador import Administrador
from app.core.security import get_senha_hash


def create_super_user(email: str, senha: str, nome: str):
    db: Session = SessionLocal()

    usuario_existente = db.query(Administrador).filter(Administrador.email == email).first()
    if usuario_existente:
        print(f"❌ O usuário {email} já existe!")
        return

    print(f"🛠️ Criando usuário {email}...")

    admin = Administrador(
        email=email,
        nome=nome,
        senha_hash=get_senha_hash(senha),
        ativo=True
    )

    db.add(admin)
    db.commit()
    print("✅ Administrador criado com sucesso!")
    db.close()


if __name__ == "__main__":
    create_super_user("admin", "admin", "Administrador")
