import sys
import os
import logging
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from alembic import command
from alembic.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.settings import settings

ALEMBIC_VERSIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "alembic", "versions")


def create_database_if_not_exists():
    db_name = settings.POSTGRES_DB
    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    host = settings.POSTGRES_HOST
    port = settings.POSTGRES_PORT

    logger.info(f"🛠️  Verificando banco de dados: {db_name}...")

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()

        if not exists:
            logger.info(f"⚠️  Banco {db_name} não encontrado. Criando...")
            cursor.execute(f"CREATE DATABASE {db_name}")
            logger.info(f"✅ Banco {db_name} criado com sucesso!")
        else:
            logger.info(f"✅ Banco {db_name} já existe.")

        cursor.close()
        conn.close()

    except Exception as e:
        logger.error(f"❌ Erro ao verificar/criar banco de dados: {e}")


def ensure_migrations_exist(alembic_cfg):
    if not os.path.exists(ALEMBIC_VERSIONS_DIR):
        os.makedirs(ALEMBIC_VERSIONS_DIR)

    versions = [f for f in os.listdir(ALEMBIC_VERSIONS_DIR) if f.endswith(".py")]

    if not versions:
        logger.warning("⚠️ Nenhuma migração encontrada. Gerando migração inicial automática...")
        try:
            command.revision(alembic_cfg, message="Migração Inicial Automática", autogenerate=True)
            logger.info("✅ Migração inicial gerada com sucesso!")
        except Exception as e:
            logger.error(f"❌ Falha ao gerar migração automática: {e}")
            logger.info("ℹ️ Verifique se seus Models estão importados no env.py do Alembic!")
            sys.exit(1)
    else:
        logger.info(f"ℹ️ Encontradas {len(versions)} migrações existentes.")


def run_migrations():
    logger.info("🔄 Preparando migrações do Alembic...")
    try:
        alembic_cfg = Config("alembic.ini")
        ensure_migrations_exist(alembic_cfg)
        logger.info("🚀 Aplicando 'upgrade head'...")
        command.upgrade(alembic_cfg, "head")
        logger.info("✅ Todas as migrações foram aplicadas!")

    except Exception as e:
        logger.error(f"❌ Erro crítico ao aplicar migrações: {e}")
        sys.exit(1)


def main():
    create_database_if_not_exists()
    run_migrations()
    logger.info("🎉 Inicialização do banco concluída com sucesso!")


if __name__ == "__main__":
    main()
