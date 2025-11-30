import sys
import os
import logging
from alembic import command
from alembic.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_migrations():
    logger.info("🔄 Iniciando atualização do banco de dados...")
    try:
        ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "alembic.ini")
        alembic_cfg = Config(ini_path)

        script_location = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "alembic")
        alembic_cfg.set_main_option("script_location", script_location)

        logger.info("🚀 Aplicando 'upgrade head'...")
        command.upgrade(alembic_cfg, "head")
        print("✅ Banco de dados atualizado com sucesso!")

    except Exception as e:
        logger.error(f"❌ Erro ao atualizar banco: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_migrations()
