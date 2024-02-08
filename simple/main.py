from robyn import Robyn
import os

host = os.getenv("APP_HOST")
port = os.getenv("APP_POR")
app = Robyn(__file__)
@app.get("/")
async def home(request):
    return f"This server running at {host}:{port}"

if __name__ == __main__:
    app.start(port=int(port), host=host)