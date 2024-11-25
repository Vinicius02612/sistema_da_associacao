from pydantic import BaseModel
from typing import List
from datetime import date, datetime

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    cpf: str
    data_nascimento: date
    senha: str
    created_at: datetime
    updated_at: datetime
    quantidade: int
    cargo: str
    dtassociacao: date


    class Config:
        orm_mode = True

class UserRequest(BaseModel):
    name: str
    email: str
    cpf: str
    data_nascimento: str
    senha: str
    quantidade: int
    cargo: str
    dtassociacao: str
    created_at: str
    updated_at: str




class SolicitacaoBase(BaseModel):
    id: int
    idUsuario: int
    usuario: UserResponse
    data: str
    status: str

    class Config:
        orm_mode = True

class SolicitacaoResponse(BaseModel):
    id: int
    idUsuario: int
    usuario: UserResponse
    data: str
    status: str

    class Config:
        orm_mode = True

class SolicitacaoRequest(BaseModel):
    idUsuario: int
    usuario: UserResponse
    data: str
    status: str

    class Config:
        orm_mode = True


class Mensalidade(BaseModel):
    id: int
    valor: float
    dataVencimento: str
    dataPagamento: str
    idSocio: int
    socio: UserResponse

    class Config:
        orm_mode = True

class MensalidadeRequest(BaseModel):
    id: int
    valor: float
    dataVencimento: str
    dataPagamento: str
    idSocio: int
    socio: UserResponse

    class Config:
        orm_mode = True

class ProjetosBase(BaseModel):
    id: int
    titulo: str
    dataInicio: str
    dataFim: str
    user_id:str

    class Config:
        orm_mode = True

class ProjetosResponse(BaseModel):
    id: int
    titulo: str
    dataInicio: str
    dataFim: str
    user_id:str

    class Config:
        orm_mode = True

class ProjetosRequest(BaseModel):
    id: int
    titulo: str
    dataInicio: str
    dataFim: str
    user_id:str

    class Config:
        orm_mode = True

class DespesaBase(BaseModel):
    id: int
    valor: float
    data: str
    origem: str

    class Config:
        orm_mode = True

class DespesaResponse(BaseModel):
    id: int
    valor: float
    data: str
    origem: str

    class Config:
        orm_mode = True

class DespesaRequest(BaseModel):
    valor: float
    data: str
    origem: str

    class Config:
        orm_mode = True



class Receitas(BaseModel):
    id: int
    valor: float
    data: str
    origem: str

    class Config:
        orm_mode = True


class ReceitasRequest(BaseModel):
    valor: float
    data: str
    origem: str

    class Config:
        orm_mode = True

class Relatorio(BaseModel):
    id: int
    despesa: List[DespesaResponse]
    receita: List[Receitas]

    class Config:
        orm_mode = True


class RelatorioRequest(BaseModel):
    id: int
    despesa: List[DespesaResponse]
    receita: List[Receitas]

    class Config:
        orm_mode = True