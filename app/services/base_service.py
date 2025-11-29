from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel
from app.repositories.base_repository import BaseRepository

T = TypeVar("T")
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)
RepoType = TypeVar("RepoType", bound=BaseRepository)


class BaseService(Generic[T, CreateSchema, UpdateSchema]):
    def __init__(self, repository: BaseRepository[T]):
        self._repository = repository

    @property
    def repository(self) -> RepoType:
        return self._repository

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self._repository.get_all(skip=skip, limit=limit)

    def get_by_id(self, model_id: int) -> Optional[T]:
        return self._repository.get_by_id(model_id)

    def create(self, obj_in: CreateSchema) -> T:
        return self._repository.create(obj_in.model_dump())

    def update(self, model_id: int, obj_in: UpdateSchema) -> Optional[T]:
        db_obj = self._repository.get_by_id(model_id)
        if not db_obj:
            return None
        return self._repository.update(db_obj, obj_in.model_dump(exclude_unset=True))

    def delete(self, model_id: int) -> bool:
        return self._repository.delete(model_id)
