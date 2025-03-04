import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    OWNER_ID = os.getenv("OWNER_ID", "0")
    TELEGRAM_API = os.getenv("TELEGRAM_API", "0")
    TELEGRAM_HASH = os.getenv("TELEGRAM_HASH", "")

    @classmethod
    def load(cls):
        """Ensure required environment variables are set"""
        for key in ["BOT_TOKEN", "OWNER_ID", "TELEGRAM_API", "TELEGRAM_HASH"]:
            value = getattr(cls, key)
            if isinstance(value, str):
                value = value.strip()
            if not value:
                raise ValueError(f"{key} variable is missing!")
