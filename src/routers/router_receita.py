from fastapi import APIRouter
from models.schemas import ReceitasRequests, ReceitasResponse
from pydantic import BaseModel
from typing import Set, Union

router = APIRouter(prefix="/receitas")


@router.get("/", response_model=list[ReceitasResponse])
def list_receitas():
    return [
        ReceitasResponse(
            id=1,
            date="12/12/1999",
            valor=100.0,
            origem="origem",
            descricao="descricao"
        ),
        ReceitasResponse(
            id=2,
            date="12/12/1999",
            valor=100.0,
            origem="origem",
            descricao="descricao"
        ),
        ReceitasResponse(
            id=3,
            date="12/12/1999",
            valor=100.0,
            origem="origem",
            descricao="descricao"
        ),
    ]

@router.post("/", response_model=ReceitasResponse, status_code=201)
def create_receitas(receitas:ReceitasRequests):
    return ReceitasResponse(**receitas.model_dump(), id=1)