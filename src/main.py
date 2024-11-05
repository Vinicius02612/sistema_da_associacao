from fastapi import FastAPI

import json
from pathlib import Path

from routers import router_receita, router_socios, router_despesas, router_projetos

app = FastAPI()



app.include_router(router_socios.router)
app.include_router(router_receita.router)
app.include_router(router_despesas.router)
app.include_router(router_projetos.router)
