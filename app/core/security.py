from passlib.context import CryptContext

hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verifica_senha(senha: str, senha_hash: str) -> bool:
    return hash_context.verify(senha, senha_hash)


def get_senha_hash(password: str) -> str:
    return hash_context.hash(password)
