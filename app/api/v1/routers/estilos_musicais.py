from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.estilo_musical import EstiloMusicalCreate, EstiloMusical, EstiloMusicalUpdate
from app.services.estilo_musical_service import EstiloMusicalService

router = APIRouter()


def get_estilo_service(db: Session = Depends(get_db)) -> EstiloMusicalService:
    return EstiloMusicalService(db)


@router.post("/", response_model=EstiloMusical, status_code=status.HTTP_201_CREATED)
def criar_estilo(estilo: EstiloMusicalCreate, service: EstiloMusicalService = Depends(get_estilo_service)):
    return service.create(estilo)


@router.get("/", response_model=List[EstiloMusical])
def listar_estilos(skip: int = 0, limit: int = 100, service: EstiloMusicalService = Depends(get_estilo_service)):
    return service.get_all(skip=skip, limit=limit)


@router.get("/{id}", response_model=EstiloMusical)
def obter_estilo(model_id: int, service: EstiloMusicalService = Depends(get_estilo_service)):
    estilo = service.get_by_id(model_id)
    if not estilo:
        raise HTTPException(status_code=404, detail="Estilo Musical não encontrado")
    return estilo


@router.put("/{id}", response_model=EstiloMusical)
def atualizar_estilo(model_id: int, estilo_in: EstiloMusicalUpdate,
                     service: EstiloMusicalService = Depends(get_estilo_service)):
    estilo = service.update(model_id, estilo_in)
    if not estilo:
        raise HTTPException(status_code=404, detail="Estilo Musical não encontrado")
    return estilo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_estilo(model_id: int, service: EstiloMusicalService = Depends(get_estilo_service)):
    sucesso = service.delete(model_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Estilo Musical não encontrado")
