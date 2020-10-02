import os
from bot import JunctionBot
from config import Config

if __name__ == "__main__":
    if not os.path.exists(Config.WORK_DIR):
        os.makedirs(Config.WORK_DIR)

    JunctionBot().run()
