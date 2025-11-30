from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permite todos os headers (Authorization, etc.)
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {
        "mensagem": "Bem-vindo à API Enciclopédia Digital do Rock!",
        "versao": "v1",
        "docs": "/docs"
    }