from fastapi import APIRouter, File, UploadFile
from models.schemas import ProjetosRequests, ProjetosResponse
from pydantic import BaseModel
from typing import Set, Union


router = APIRouter(prefix="/projetos")

@router.get("/", response_model=list[ProjetosResponse])
def  list_projetos():
    return [
        ProjetosResponse(
            id=1,
            nome="nome",
            descricao="descricao",
            dataInicio="12/12/1999",
            dataFim="12/12/1999",
            valor=100.0
        ),
        ProjetosResponse(
            id=2,
            nome="nome",
            descricao="descricao",
            dataInicio="12/12/1999",
            dataFim="12/12/1999",
            valor=100.0
        ),
        ProjetosResponse(
            id=3,
            nome="nome",
            descricao="descricao",
            dataInicio="12/12/1999",
            dataFim="12/12/1999",
            valor=100.0
        ),
    ]


@router.post("/", response_model=ProjetosResponse, status_code=201)
def create_projetos(projetos:ProjetosRequests, file: UploadFile = File(...)):

    return ProjetosResponse(**projetos.model_dump(), id=1)