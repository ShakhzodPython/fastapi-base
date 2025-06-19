from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel, PostgresDsn

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv())

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class APIV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    auth: str = "/auth"
    messages: str = "/messages"

class APIPrefix(BaseModel):
    prefix: str = "/api"
    v1: APIV1Prefix = APIV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        """Bearer token url for fastapi-users"""
        # api/v1/auth/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


# Config for fastapi-users
class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_secret: str
    verification_token_secret: str


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
        env_file=(".env", ".env.template"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()
    db: DatabaseConfig
    access_token: AccessToken

settings = Settings()
