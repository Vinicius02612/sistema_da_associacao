# AQBA - SISTEMA PARA GERENCIAMENTO DA ASSOCIAÇÃO QUILOMBOLA BREJÃO DOS AIPINS

# Descrição

Este repositório se destina para o desenvolvimento do sistema da associação da Comunidade Quilombola Brejão dos Aipins

# Tecnologias Utilizadas

# Frontend

Vue.js

Vuetify

NodeJS

# Backend

Python

FastAPI

Pydantic (para gerenciamento de schemas)

SQLAlchemy (para gerenciamento de tabelas do banco de dados)

PostgreSQL

Docker (para conteinerização)

# Requisitos

Certifique-se de ter instalado os seguintes softwares antes de iniciar o projeto:

Node.js (para executar o frontend)

Docker (para conteinerização do backend e banco de dados)

Python 3.10+ (caso deseje rodar o backend sem Docker)

# Como Rodar o Projeto

## Clonando o Repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## Rodando com Docker

Instale o docker e docker-compose


## Rodando Manualmente

Backend

Instale as dependências do backend: 

```
sudo apt-get update
sudo apt-get install ./docker-desktop-amd64.deb

```


```
cd Backend

pip install -r requirements.txt 
```

Execute o backend:

``` 
uvicorn main:app --reload 
```

Frontend

Instale as dependências do frontend:

``` 
cd Frontend 
npm install 
```

Execute o frontend:

``` 
npm run dev
```


# Estrutura do Projeto

```
/sistema_da_associacao
|-- /Backend
    | -- /  # Código do backend com FastAPI
|-- /Frontend
    |--   # Código do frontend com Vue.js e Vuetify
|-- docker-compose.yml  # Configuração do Docker
|-- README.md  # Este arquivo
```

# Tabela de Versões (Implementação do Figma)

| Titulo       | Descrição                       | Data           | Responsável                                        | 
| :---         |     :---:                       | :---           |      ---:                                          |
| Tela login   | Protótipo da tela de Login  e Cadastro |  07/04/2025    | Mayra Caetano[GitHub:](https://github.comMay-Raa)  |
| Tela Adminstrador   | Protótipo da tela Sócio   |  07/04/2025    | Mayra Caetano[GitHub:](https://github.com/May-Raa) |
| Tela listagem de Sócios | Tabela com a lista de Sócios cadastrados| 08/04/2025 | Mayra Caetano[GitHub:](https://github.com/May-Raa) |
| Tela Adicionar Sócio | Protótipo da tela de adicionar Sócio | 08/04/2025 | Mayra Caetano[GitHub:](https://github.com/May-Raa) |




# Contribuição

<img src="https://github.com/aleffericlys.png" width="100" height="100" style="border-radius: 50%;" > <h3>Alef Fericlys[GitHub:](https://github.com/aleffericlys)</h3> 

<img src="https://github.com/Vinicius02612.png" width="100" height="100" style="border-radius: 50%;"><h3>Vinicius Nunes[GitHub:](https://github.com/Vinicius02612)</h3> 

<img src="https://github.com/May-Raa.png" width="100" height="100" style="border-radius: 50%;" ><h3>Mayra Caetano[GitHub:](https://github.com/May-Raa) 
</h3> 

<img src="https://github.com/Mrprince0421.png" width="100" height="100" style="border-radius: 50%;" ><h3>\Marcos Eduardo[GitHub:](https://github.com/Mrprince0421) 
</h3> 

