from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str="LLMOPS_RAG"
    API_V1_STR:str="/api/v1"

settings=Settings()    