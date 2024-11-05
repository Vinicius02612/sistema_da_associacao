from fastapi import APIRouter
from models.schemas import DespesasResponse, DespesasResquests
from pydantic import BaseModel
from typing import Set, Union

router = APIRouter(prefix="/despesas")

@router.get("/", response_model=list[DespesasResponse])
def list_despesas():
    return [
        DespesasResponse(
            id=1,
            date="12/12/1999",
            valor=100.0,
            origem="origem",
            descricao="descricao"
        ),
        DespesasResponse(
            id=2,
            date="12/12/1999",
            valor=100.0,
            origem="origem",
            descricao="descricao"
        ),
        DespesasResponse(
            id=3,
            date="12/12/1999",
            valor=100.0,
            origem="origem",
            descricao="descricao"
        ),
    ]

@router.post("/", response_model=DespesasResponse, status_code=201)
def create_despesas(despesas:DespesasResquests):
    return DespesasResponse(**despesas.model_dump(), id=1)