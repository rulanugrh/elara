from robyn import Robyn
from src.controller import todo
from config import config

conf = config.GetConfig()

app = Robyn(__file__)
@app.get("/")
async def home(request):
    return f"This server running at {conf.APP_HOST}:{conf.APP_PORT}"

app.include_router(todo.todo_router)

if __name__ == __main__:
    app.start(port=int(conf.APP_PORT), host=conf.APP_HOST)