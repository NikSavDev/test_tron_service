from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    address: str
    api_key: str

    model_config = {
        'env_file': '.env'
    }

settings = Settings()