from robyn import Robyn
from src.controller import user
from config import config

conf = config.GetConfig()
app = Robyn(__file__)
app.include_router(user.user_router)

if __name__ == __main__:
    app.start(host=conf.APP_HOST, port=int(conf.APP_PORT))
