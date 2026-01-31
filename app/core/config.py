from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Todo API V1"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int= 60

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()