from fastapi import APIRouter
from models.schemas import SocioResponse, SocioRequest
from pydantic import BaseModel
from typing import Set, Union

router = APIRouter(prefix="/socios")



@router.get("/", response_model=list[SocioResponse])
def listar_socios():
    return [
        SocioResponse(
            id=1,
            nome="vinicius",
            email="viniciusnunes02612@gmail.com",
            cpf="12345678910",
            senha="123",
            tipo="admin", # 'admin' ou 'comum'
            dataDeNascimento="12/12/1999",
            quantidadePessoas=1,
            imagem=None
        ),
         SocioResponse(
            id=2,
            nome="vinicius",
            email="viniciusnunes02612@gmail.com",
            cpf="12345678910",
            senha="123",
            tipo="admin", # 'admin' ou 'comum'
            dataDeNascimento="12/12/1999",
            quantidadePessoas=1,
            imagem=None
        ),
         SocioResponse(
            id=3,
            nome="vinicius",
            email="viniciusnunes02612@gmail.com",
            cpf="12345678910",
            senha="123",
            tipo="admin", # 'admin' ou 'comum'
            dataDeNascimento="12/12/1999",
            quantidadePessoas=1,
            imagem=None
        ),
    ]

@router.post("/", response_model=SocioResponse, status_code=201)
def criar_socio(socio:SocioRequest):
    return SocioResponse(**socio.model_dump(), id=1)