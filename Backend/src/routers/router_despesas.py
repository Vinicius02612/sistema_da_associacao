from fastapi import APIRouter,Depends,HTTPException
from schemas.schema import DespesaResponse, DespesaRequest
from typing import List
from sqlalchemy.orm import Session
from connection.dependences import get_db
from models.models import Despesas, User
from services.security import (get_current_user)
from services.permissions import president_permission


router = APIRouter(prefix="/despesas")

#retorna todas as despesas em forma de lista
@router.get("/", response_model=List[DespesaResponse])
def get_despesas(db:Session = Depends(get_db)) -> List[Despesas]:
    
    despesas = db.query(Despesas).all()
    if not despesas:
        raise HTTPException(status_code=404, detail="Não há despesas cadastradas")
    return despesas


@router.post("/", response_model=DespesaResponse, status_code=201)
def post_despesas(despesa: DespesaRequest, db: Session = Depends(get_db)) -> Despesas:
    new_despesa = Despesas(
        **despesa.model_dump()
    )
    db.add(new_despesa)
    db.commit()
    db.refresh(new_despesa)

    return new_despesa

@router.put("/{id}", response_model=DespesaResponse)
def despesas_update(id:int, despesa_request: DespesaRequest, db: Session = Depends(get_db)) -> Despesas:
    despesa = db.query(Despesas).filter(Despesas.id == id).first()
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    for key, value in despesa_request.model_dump().items():
        setattr(despesa, key, value)
   
    db.commit()
    db.refresh(despesa)
    return despesa


@router.delete("/{id}", response_model=DespesaResponse)
def despesas_delete(id:int, db: Session = Depends(get_db)) -> Despesas:

    despesa = db.query(Despesas).filter(Despesas.id == id).first()
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    db.delete(despesa)
    db.commit()
    return despesa