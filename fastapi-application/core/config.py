from pathlib import Path

from pydantic import BaseModel, PostgresDsn

from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
ENV_TEMPLATE_PATH = Path(__file__).resolve().parents[1] / ".env.template"


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class APIPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_conventions: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",  # naming of index
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",  # naming of unique constrains
        "ck": "ck_%(table_name)s_%(constraint_name)s",  # naming of check constrains
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # naming of foreign key
        "pk": "pk_%(table_name)s",  # naming of primary key
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            str(ENV_TEMPLATE_PATH),
            str(
                ENV_PATH,
            ),
        ),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()
    db: DatabaseConfig


settings = Settings()
