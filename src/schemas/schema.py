from pydantic import BaseModel
from typing import List

class UserResponse(BaseModel):
    id: int
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




class Solicitacao(BaseModel):
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

class Projetos(BaseModel):
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

class Despesa(BaseModel):
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
    despesa: List[Despesa]
    receita: List[Receitas]

    class Config:
        orm_mode = True


class RelatorioRequest(BaseModel):
    id: int
    despesa: List[Despesa]
    receita: List[Receitas]

    class Config:
        orm_mode = True