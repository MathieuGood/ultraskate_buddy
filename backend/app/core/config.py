from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./dev.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
    )


settings = Settings()
