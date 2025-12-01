from pydantic_settings import BaseSettings, SettingsConfigDict
import os

env_file_path = os.environ.get("ENV_FILE", ".env")


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Enciclopédia Digital do Rock"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=env_file_path if os.path.exists(env_file_path) else None,
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra='ignore'
    )


settings = Settings()
