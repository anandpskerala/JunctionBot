import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    JUNCTION_CHATS = set(int(x) for x in os.environ.get("JUNCTION_CHATS", "").split())
    SESSION_NAME = "JunctionBot"
    WORKERS = 200
    WORK_DIR = "bot/working_dir"
