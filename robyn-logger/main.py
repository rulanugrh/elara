from robyn import Robyn, Router
from src.controller import user, todo
from config import config

conf = config.GetConfig()
app = Robyn(__file__)

@app.exception
def handle_exception(error):
    return {"status_code": 500, "msg": f"something error: {error}"}


app.include_router(user.user_router)
app.include_router(todo.todo_router)

if __name__ == __main__:
    app.start(host=conf.APP_HOST, port=int(conf.APP_PORT))
