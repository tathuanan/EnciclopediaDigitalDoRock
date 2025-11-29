from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.album import AlbumCreate, Album, AlbumUpdate
from app.services.album_service import AlbumService

router = APIRouter()


def get_album_service(db: Session = Depends(get_db)) -> AlbumService:
    return AlbumService(db)


@router.post("/", response_model=Album, status_code=status.HTTP_201_CREATED)
def criar_album(album: AlbumCreate, service: AlbumService = Depends(get_album_service)):
    return service.create(album)


@router.get("/", response_model=List[Album])
def listar_albuns(skip: int = 0, limit: int = 100, service: AlbumService = Depends(get_album_service)):
    return service.get_all(skip=skip, limit=limit)


@router.get("/{id}", response_model=Album)
def obter_album(model_id: int, service: AlbumService = Depends(get_album_service)):
    album = service.get_by_id(model_id)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum não encontrado")
    return album


@router.put("/{id}", response_model=Album)
def atualizar_album(model_id: int, album_in: AlbumUpdate, service: AlbumService = Depends(get_album_service)):
    album = service.update(model_id, album_in)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum não encontrado")
    return album


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_album(model_id: int, service: AlbumService = Depends(get_album_service)):
    sucesso = service.delete(model_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Álbum não encontrado")
