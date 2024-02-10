from robyn import SubRouter, Request
from config.config import *
from repository import user
import json
from logging import Logger

user_router = SubRouter(__name__, prefix="/api/v1/user")
sessionLocal = GetConnection()
logs = Logger(user_router)

@user_router.before_request("/request")
async def log_request_register(request: Request):
    logs.info(f"Receive request from {request}")

@user_router.before_request("/login")
async def log_request_login(request: Request):
    logs.info(f"Receive request from {request}")

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