from pydantic import BaseSettings, Field


class ApiConfig(BaseSettings):

    DEBUG: bool = Field(env='DEBUG', default=True)
