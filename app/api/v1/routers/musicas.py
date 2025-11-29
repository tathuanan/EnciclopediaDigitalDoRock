from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.musica import MusicaCreate, Musica, MusicaUpdate
from app.services.musica_service import MusicaService

router = APIRouter()

def get_musica_service(db: Session = Depends(get_db)) -> MusicaService:
    return MusicaService(db)

@router.post("/", response_model=Musica, status_code=status.HTTP_201_CREATED)
def criar_musica(musica: MusicaCreate, service: MusicaService = Depends(get_musica_service)):
    return service.create(musica)

@router.get("/", response_model=List[Musica])
def listar_musicas(skip: int = 0, limit: int = 100, service: MusicaService = Depends(get_musica_service)):
    return service.get_all(skip=skip, limit=limit)

@router.get("/{id}", response_model=Musica)
def obter_musica(model_id: int, service: MusicaService = Depends(get_musica_service)):
    musica = service.get_by_id(model_id)
    if not musica:
        raise HTTPException(status_code=404, detail="Música não encontrada")
    return musica

@router.put("/{id}", response_model=Musica)
def atualizar_musica(model_id: int, musica_in: MusicaUpdate, service: MusicaService = Depends(get_musica_service)):
    musica = service.update(model_id, musica_in)
    if not musica:
        raise HTTPException(status_code=404, detail="Música não encontrada")
    return musica

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_musica(model_id: int, service: MusicaService = Depends(get_musica_service)):
    sucesso = service.delete(model_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Música não encontrada")