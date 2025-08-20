from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "crud-task-manager"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
