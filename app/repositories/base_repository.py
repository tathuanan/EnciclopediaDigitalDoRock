from typing import Generic, TypeVar, Type, List, Optional, Any
from sqlalchemy.orm import Session
from app.core.base import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self, db: Session, modelo: Type[T]):
        self._db = db
        self._modelo = modelo

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self._db.query(self._modelo).offset(skip).limit(limit).all()

    def get_by_id(self, modelo_id: int) -> Optional[T]:
        return self._db.query(self._modelo).filter(self._modelo.id == modelo_id).first()  # type: ignore

    def create(self, obj_in: dict) -> T:
        db_obj = self._modelo(**obj_in)
        self._db.add(db_obj)
        self._db.commit()
        self._db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: T, obj_in: dict) -> T:
        for field, value in obj_in.items():
            setattr(db_obj, field, value)

        self._db.add(db_obj)
        self._db.commit()
        self._db.refresh(db_obj)
        return db_obj

    def delete(self, modelo_id: int) -> bool:
        obj = self._get_by_id(modelo_id)
        if obj:
            self._db.delete(obj)
            self._db.commit()
            return True
        return False

    def filter_by_ilike(self, coluna: Any, termo: str) -> List[T]:
        return self._db.query(self._modelo).filter(coluna.ilike(f"%{termo}%")).all()
