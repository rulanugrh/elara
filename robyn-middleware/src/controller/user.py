from robyn import SubRouter
from config.config import *
from repository import user
import json
from middleware import verify

user_router = SubRouter(__name__, prefix="/api/v1/user")
sessionLocal = GetConnection()

@user_router.post("/register")
async def register(request):
    req = request.json()
    with sessionLocal as db:
        create_user = user.create_user(db, req)
    
    if create_user is None:
        raise Exception("Cant create user")
        
    return {
        "status_code": 200,
        "msg": "sucess create user"
    }
    
@user_router.post("/login")
async def login(request):
    req = request.json()
    with sessionLocal as db:
        token = user.authenticate_user(db, **req)
    
    if token is None:
        raise Exception("Invalid credentials")
    
    return {
        "status_code": 200,
        "msg": "sucess create user",
        "token": token
    }