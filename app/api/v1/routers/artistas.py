from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.artista import ArtistaCreate, Artista, ArtistaUpdate
from app.services.artista_service import ArtistaService

router = APIRouter()


def get_artista_service(db: Session = Depends(get_db)) -> ArtistaService:
    return ArtistaService(db)


@router.post("/", response_model=Artista, status_code=status.HTTP_201_CREATED)
def criar_artista(artista: ArtistaCreate, service: ArtistaService = Depends(get_artista_service)):
    return service.create(artista)


@router.get("/", response_model=List[Artista])
def listar_artistas(skip: int = 0, limit: int = 100, service: ArtistaService = Depends(get_artista_service)):
    return service.get_all(skip=skip, limit=limit)


@router.get("/{id}", response_model=Artista)
def obter_artista(model_id: int, service: ArtistaService = Depends(get_artista_service)):
    artista = service.get_by_id(model_id)
    if not artista:
        raise HTTPException(status_code=404, detail="Artista não encontrado")
    return artista


@router.put("/{id}", response_model=Artista)
def atualizar_artista(model_id: int, artista_in: ArtistaUpdate, service: ArtistaService = Depends(get_artista_service)):
    artista = service.update(model_id, artista_in)
    if not artista:
        raise HTTPException(status_code=404, detail="Artista não encontrado")
    return artista


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_artista(model_id: int, service: ArtistaService = Depends(get_artista_service)):
    sucesso = service.delete(model_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Artista não encontrado")
