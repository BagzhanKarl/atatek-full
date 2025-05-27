from pydantic_settings import BaseSettings, SettingsConfigDict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    HOST: str = 'localhost'
    PORT: int = 5432
    USER: str = 'jaai_admin'
    PASSWORD: str = 'jaai_admin'
    BASE: str = 'jaai_base'

    JWT_SECRET_KEY: str = 'secret'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info(f"Database settings: HOST={self.HOST}, PORT={self.PORT}, USER={self.USER}, BASE={self.BASE}")

    @property
    def get_base_link(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.BASE}"
    
    @property
    def get_base_link_for_alembic(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.BASE}?async_fallback=true"
    
    @property
    def get_jwt_secret_key(self):
        return self.JWT_SECRET_KEY
    
    model_config = SettingsConfigDict(
        env_file=None,
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore'
    )
    
    
settings = Settings()
    
