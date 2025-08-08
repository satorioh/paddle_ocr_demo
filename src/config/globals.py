from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # -------------路由配置----------------- #
    API_PREFIX: str = "/py-api"


settings = Settings()
