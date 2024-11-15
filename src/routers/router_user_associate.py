from fastapi import APIRouter
from schemas.schema import User, UserRequest
from typing import List

router = APIRouter(prefix="/rotuers")

#retorna todos os associados em forma de lista


@router.get("/", response_model=List[User])
def get_user_associates():
    return [
        User(
            id=1,
            name="João",
            email="vinicius@nunes",
            cpf="123456789",
            data_nascimento="12/12/12",
            senha="123456",
            quantidade=1,
            cargo="admin",
            dtassociacao="12/12/12",
            created_at="12/12/12",
            updated_at="12/12/12"
        ),
        User(
            id=2,
            name="maria",
            email="maria@nunes",
            cpf="123456789",
            data_nascimento="12/12/12",
            senha="123456",
            quantidade=1,
            cargo="admin",
            dtassociacao="12/12/12",
            created_at="12/12/12",
            updated_at="12/12/12"
        )
    ]


@router.post("/", response_model=User, status_code=201)
def create_user_associate(user: UserRequest):

    return User(
        id=1,
        name=user.name,
        email=user.email,
        cpf=user.cpf,
        data_nascimento=user.data_nascimento,
        senha=user.senha,
        quantidade=user.quantidade,
        cargo=user.cargo,
        dtassociacao=user.dtassociacao,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
