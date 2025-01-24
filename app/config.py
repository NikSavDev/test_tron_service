from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    address: str

    model_config = {
        'env_file': '.env'
    }

settings = Settings()