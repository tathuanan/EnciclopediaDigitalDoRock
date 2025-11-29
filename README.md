# Enciclopédia Digital do Rock 🎸

Esta aplicação foi desenvolvida para organizar e consultar informações sobre bandas, álbuns e artistas do rock.

O projeto segue rigorosamente os princípios de Clean Architecture e SOLID, garantindo escalabilidade, testabilidade e facilidade de manutenção.

## 🚀 Tecnologias Utilizadas
- Linguagem: Python 3.12+
- Framework Web: FastAPI
- Banco de Dados: PostgreSQL
- ORM: SQLAlchemy (Gerenciamento de dados)
- Migrações: Alembic (Controle de versão do banco)
- Gerenciador de Pacotes: Poetry
- Validação de Dados: Pydantic V2

## 🏛️ Arquitetura do Projeto

O sistema foi desenhado utilizando uma arquitetura em camadas para separar responsabilidades (Separation of Concerns):

### **Camada de Apresentação (API/Rotas)**
📁 `app/api/v1/routers`

Responsável por:
- Receber requisições HTTP
- Validar entradas (Schemas)
- Retornar respostas

### **Camada de Serviços (Regras de Negócio)**
📁 `app/services`

Contém:
- Regras de negócio
- Processamento de dados

Encapsula o acesso aos repositórios.

### **Camada de Acesso aos Dados (Repositórios)**
📁 `app/repositories`

Responsável por:
- Comunicação com o banco de dados
- CRUD com SQL
- Padrão **Repository Pattern** com `BaseRepository` genérica

### **Camada de Domínio (Modelos & DTOs)**
- 📁 `app/models` → Tabelas do banco (SQLAlchemy)
- 📁 `app/schemas` → DTOs e validação (Pydantic)

---

## 🛠️ Configuração e Execução Local

### 1. Pré-requisitos

Certifique-se de ter instalado:

- Python 3.12+
- PostgreSQL (Rodando localmente ou via Docker)
- Git (Para clonar o projeto)

### 2. Instalação de pacotes necessários
Se você ainda não tem o Poetry, instale-o e configure o PATH: (no Windowns preferível a utilização do PowerShell)

```bash
# Instala o Poetry
pip install poetry

# Adiciona ao PATH (Execute apenas se o comando 'poetry' não for reconhecido)
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:USERPROFILE\AppData\Roaming\Python\Python312\Scripts", "User")

# Feche e reabra o terminal e verifique se o comando poetry agora é reconhecido
```

Clone o repositório e instale as dependências:
```bash
# Instala as dependências do projeto
poetry install
```

### 3. Configuração do Ambiente (.env)

Altere o arquivo chamado .env na raiz do projeto.

```
POSTGRES_USER=seu_usuario_postgres_aqui
POSTGRES_PASSWORD=sua_senha_postgres_aqui
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=o_nome_do_seu_banco_aqui
```

### 4. Inicializando o Banco de Dados

Foi criado um script utilitário para facilitar a configuração inicial.

**Passo A: Criar Banco e Tabelas.** Este comando cria o banco conforme o nome setado em POSTGRES_DB no arquivo .env (se não existir) e roda as migrações do Alembic.
```bash
# Nota: Se você fez alterações nos Models e precisa gerar uma nova migration
# antes de rodar o comando abaixo, use: poetry run alembic revision --autogenerate -m "descricao da mudanca"

poetry run python scripts/init_db.py
```

**Passo B: Criar Usuário Administrador.** Para integração com o Front-End como o sistema possui um administrador único gerenciado via banco, crie-o com este comando:
```bash
# Edite o arquivo scripts/create_admin.py se quiser mudar o email/senha padrão

poetry run python scripts/create_admin.py
```
### 5. Rodando a Aplicação

Inicie o servidor de desenvolvimento:

```bash
poetry run uvicorn main:app --reload
```
Acesse a documentação interativa (Swagger UI) em:👉 http://localhost:8000/docs

🧪 Estrutura de Pastas
```
app/
├── api/            # Rotas da API (v1)
├── core/           # Configurações globais (DB, Settings, Security)
├── models/         # Modelos do SQLAlchemy (Tabelas)
├── repositories/   # Camada de acesso a dados (CRUD)
├── schemas/        # Schemas Pydantic (Validação)
└── services/       # Regras de Negócio
scripts/            # Scripts auxiliares (Init DB, Create Admin)
main.py             # Ponto de entrada da aplicação
alembic.ini         # Configuração de migrações
```