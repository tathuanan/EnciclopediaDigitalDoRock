from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.instrumento import InstrumentoCreate, Instrumento, InstrumentoUpdate
from app.services.instrumento_service import InstrumentoService

router = APIRouter()


def get_instrumento_service(db: Session = Depends(get_db)) -> InstrumentoService:
    return InstrumentoService(db)


@router.post("/", response_model=Instrumento, status_code=status.HTTP_201_CREATED)
def criar_instrumento(instrumento: InstrumentoCreate, service: InstrumentoService = Depends(get_instrumento_service)):
    return service.create(instrumento)


@router.get("/", response_model=List[Instrumento])
def listar_instrumentos(skip: int = 0, limit: int = 100,
                        service: InstrumentoService = Depends(get_instrumento_service)):
    return service.get_all(skip=skip, limit=limit)


@router.get("/{id}", response_model=Instrumento)
def obter_instrumento(model_id: int, service: InstrumentoService = Depends(get_instrumento_service)):
    obj = service.get_by_id(model_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Instrumento não encontrado")
    return obj


@router.put("/{id}", response_model=Instrumento)
def atualizar_instrumento(model_id: int, instrumento_in: InstrumentoUpdate,
                          service: InstrumentoService = Depends(get_instrumento_service)):
    obj = service.update(model_id, instrumento_in)
    if not obj:
        raise HTTPException(status_code=404, detail="Instrumento não encontrado")
    return obj


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_instrumento(model_id: int, service: InstrumentoService = Depends(get_instrumento_service)):
    sucesso = service.delete(model_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Instrumento não encontrado")
