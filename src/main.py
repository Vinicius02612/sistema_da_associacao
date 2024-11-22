import uvicorn
from fastapi import FastAPI, HTTPException,status
from routers import router_user_associate
from connection.database import Base, engine
from models.models import User


#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_user_associate.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)