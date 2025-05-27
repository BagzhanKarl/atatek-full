from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str = 'localhost'
    PORT: int = 5432
    USER: str = 'jaai_admin'
    PASSWORD: str = 'jaai_admin'
    BASE: str = 'jaai_base'

    JWT_SECRET_KEY: str = 'secret'

    @property
    def get_base_link(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.BASE}"
    
    @property
    def get_base_link_for_alembic(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.BASE}?async_fallback=true"
    
    @property
    def get_jwt_secret_key(self):
        return self.JWT_SECRET_KEY
    
    model_config = SettingsConfigDict(env_file='.env')
    
    
settings = Settings()
    
