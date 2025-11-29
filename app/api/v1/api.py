from fastapi import APIRouter
from app.api.v1.routers import bandas, albuns, artistas, estilos_musicais, instrumentos, musicas

api_router = APIRouter()

api_router.include_router(artistas.router, prefix="/artistas", tags=["Artistas"])
api_router.include_router(albuns.router, prefix="/albuns", tags=["Álbuns"])
api_router.include_router(bandas.router, prefix="/bandas", tags=["Bandas"])
api_router.include_router(estilos_musicais.router, prefix="/estilos-musicais", tags=["Estilos Musicais"])
api_router.include_router(instrumentos.router, prefix="/instrumentos", tags=["Instrumentos"])
api_router.include_router(musicas.router, prefix="/musicas", tags=["Músicas"])
