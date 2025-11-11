# Enciclopédia Digital do Rock 🎸

Aplicação desenvolvida em **FastAPI** com **SQLAlchemy**, **Pydantic**, e **Alembic** 
voltada à organização e consulta de informações sobre bandas, álbuns e artistas do rock.

## 🚀 Tecnologias
- Alembic
- FastAPI
- SQLAlchemy
- Pydantic
- Poetry

## 🛠️ Execução local

### OBS: Para execução no Windows é necessário ter o python instalado para rodar o comando pip abaixo

```bash
pip install poetry
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:USERPROFILE\AppData\Roaming\Python\Python312\Scripts", "User")
poetry install
poetry run uvicorn app.main:app --reload
