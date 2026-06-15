import os

class Config:
    def __init__(self):
        pass

    def db_config(self) -> dict[str, str]:
        return {
            "DB_USER": os.getenv("DB_USER", ""),
            "DB_PASSWORD": os.getenv("DB_PASSWORD", ""),
            "DB_HOST": os.getenv("DB_HOST", "localhost"),
            "DB_PORT": os.getenv("DB_PORT", "5432"),
            "DB_NAME": os.getenv("DB_NAME", ""),
        }