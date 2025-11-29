from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.banda import BandaCreate, Banda, BandaUpdate
from app.services.banda_service import BandaService

router = APIRouter()


def get_banda_service(db: Session = Depends(get_db)) -> BandaService:
    return BandaService(db)


@router.post("/", response_model=Banda, status_code=status.HTTP_201_CREATED)
def criar_banda(banda: BandaCreate, service: BandaService = Depends(get_banda_service)):
    return service.create(banda)


@router.get("/", response_model=List[Banda])
def listar_bandas(skip: int = 0, limit: int = 100, service: BandaService = Depends(get_banda_service)):
    return service.get_all(skip=skip, limit=limit)


@router.get("/{id}", response_model=Banda)
def obter_banda(model_id: int, service: BandaService = Depends(get_banda_service)):
    banda = service.get_by_id(model_id)
    if not banda:
        raise HTTPException(status_code=404, detail="Banda não encontrada")
    return banda


@router.put("/{id}", response_model=Banda)
def atualizar_banda(model_id: int, banda_in: BandaUpdate, service: BandaService = Depends(get_banda_service)):
    banda = service.update(model_id, banda_in)
    if not banda:
        raise HTTPException(status_code=404, detail="Banda não encontrada")
    return banda


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_banda(model_id: int, service: BandaService = Depends(get_banda_service)):
    sucesso = service.delete(model_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Banda não encontrada")
