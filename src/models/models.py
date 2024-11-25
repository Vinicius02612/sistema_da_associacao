from sqlalchemy import Column, Date,DateTime, ForeignKey, Integer, String, Float, Table

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from connection.database import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    cpf = Column(String, index=True)
    data_nascimento = Column(Date)
    senha = Column(String)
    quantidade = Column(Integer)
    cargo = Column(String)
    dtassociacao = Column(Date)
    mensalidades = relationship("Mensalidade", back_populates="socio", cascade="all, delete-orphan")
    projetos = relationship("Projetos", back_populates="socios", cascade="all, delete-orphan")
    solicitacoes = relationship("Solicitacao", back_populates="user", cascade="all, delete-orphan")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Solicitacao(Base):
    __tablename__ = 'solicitacoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('user.id'))
    data = Column(Date)
    status = Column(String)
    user = relationship("User", back_populates="solicitacoes")



class Mensalidade(Base):
    __tablename__ = 'mensalidades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float)
    dtvencimento = Column(Date)
    dtpsagamento = Column(Date)
    idsocio = Column(Integer, ForeignKey('user.id'))
    # Relacionamento com User
    socio = relationship("User", back_populates="mensalidades")


class Projetos(Base):
    __tablename__ = 'projetos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    dtinicio = Column(Date)
    dtfim = Column(Date)
    # Relacionamento com User
    socios = relationship("User", secondary="user_projetos", back_populates="projetos")
    
class Despesas(Base):
    __tablename__ = 'despesas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float)
    data = Column(Date)
    origem = Column(String)



class Receitas(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    data = Column(Date)
    origem = Column(String)
   


class Relatorio(Base):
    __tablename__ = 'relatorios'
    id = Column(Integer, primary_key=True)
    data = Column(Date)
    idDespesa = Column(Integer, ForeignKey('despesas.id'))
    idReceita = Column(Integer, ForeignKey('receitas.id'))
    despesa = relationship("Despesas", back_populates="relatorios")
    receita = relationship("Receitas", back_populates="relatorios")


# Tabela de associação para User e Projetos
user_projetos = Table(
    'user_projetos',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('projeto_id', Integer, ForeignKey('projetos.id'))
)