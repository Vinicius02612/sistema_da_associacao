from pydantic import BaseModel
from typing import Set, Union


class ImageResponse(BaseModel):
    id:int
    nome:str
    url:str

class ImageResquest(BaseModel):
    id:int
    nome:str
    url:str

class SocioResponse(BaseModel):
    id:int
    nome:str
    email:str
    cpf:str
    senha:str
    tipo:str # 'admin' ou 'comum'
    dataDeNascimento:str
    quantidadePessoas:int
    imagem:Union[ImageResponse, None]

class SocioRequest(BaseModel):
    nome:str
    email:str
    cpf:str
    senha:str
    tipo:str # 'admin' ou 'comum'
    dataDeNascimento:str
    quantidadePessoas:int
    imagem:Union[ImageResquest, None]

class ReceitasResponse(BaseModel):
    id:int
    date:str
    valor:float
    origem:str
    descricao:str


class ReceitasRequests(BaseModel):
    date:str
    valor:float
    origem:str
    descricao:str


class DespesasResponse(BaseModel):
    id:int
    date:str
    valor:float
    origem:str
    descricao:str


class DespesasResquests(BaseModel):
    date:str
    valor:float
    origem:str
    descricao:str


#Criar a classe relatorio que contenha os dados de receitas e despesas
class Relatorio(BaseModel):
    id:int
    dataRelatorio:str
    receitas:Union[ReceitasResponse, None]
    despesas:Union[DespesasResponse, None]
    saldo:float


class ProjetosResponse(BaseModel):
    id:int
    titulo:str
    dataInicio:str
    dataFim:str
    caminhoArquivo:str
    status:str
    nomeOrganizacao:str
    documento:str

class ProjetosRequests(BaseModel):
    titulo:str
    dataInicio:str
    dataFim:str
    caminhoArquivo:str
    status:str
    nomeOrganizacao:str
    documento:str