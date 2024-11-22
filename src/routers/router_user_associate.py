from fastapi import APIRouter,Depends
from schemas.schema import UserResponse, UserRequest
from typing import List
from sqlalchemy.orm import Session
from connection.dependences import get_db
from models.models import User 
#importar Dependes para usar o banco de dados



router = APIRouter(prefix="/users")

#retorna todos os associados em forma de lista


@router.get("/", response_model=List[UserResponse])
def get_user_associates(db:Session = Depends(get_db)) -> List[UserResponse]:
    user = db.query(User).all()
    return user


@router.post("/", response_model=UserResponse, status_code=201)
def create_user_associate(user_request: UserRequest, db: Session = Depends(get_db)) -> User:
    new_user = User(
        **user_request.model_dump()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return User(**new_user.model_dump())
