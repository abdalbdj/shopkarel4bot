import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("7133001036:AAHhM_t0yfgjWQUSSX7MpPiET1gvl9vJgC8", "")

    APP_ID = int(os.environ.get("APP_ID", 27596357))

    API_HASH = os.environ.get("API_HASH", "6332fa4e311625ad32a403349cb41ed9")
