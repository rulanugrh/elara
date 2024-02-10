from robyn import SubRouter, Response, Request
from repository import todo
from logging import Logger
from config.config import GetConnection

todo_router = SubRouter(__name__, prefix="/api/v1/todo")
sessionlocal = GetConnection()
logs = Logger(todo_router)

@todo_router.before_request("/create")
async def log_request_create_todo(request: Request):
    logs.info(f"Receive request from {request}")

@todo_router.before_request("/find")
async def log_request_find_all_todo(request: Request):
    logs.info(f"Receive request from {request}")

@todo_router.before_request("/find/:id")
async def log_request_find_by_id_todo(request: Request):
    logs.info(f"Receive request from {request}")

@todo_router.before_request("/delete/:id")
async def log_request_delete_todo(request: Request):
    logs.info(f"Receive request from {request}")

@todo_router.before_request("/update/:id")
async def logs_update_todo(request: Request):
    logs.info(f"Receive request from {request}")

@todo_router.post("/create")
async def create_todo(request: Request):
    with sessionlocal as db:
        todo = request.json()
        response = todo.create_todo(db, todo)
    
    if response is None:
        raise Exception("todo not added to db")
    
    return {
        "status_code": 200,
        "description": "success added todo",
        "data": response
    }

@todo_router.get("/find/:id")
async def get_todo_by_id(request: Request):
    id = int(request.path_params.get("id"))
    with sessionlocal as db:
        response = todo.get_todo_by_id(db, id)
    
    if response is None:
        raise Exception(f"sorry todo with this {id} not found")
    
    return {
        "status_code": 200,
        "description": f"todo with {id} found",
        "data": response
    }

@todo_router.get("/find")
async def get_all_todo(request: Request):
    with sessionlocal as db:
        response = todo.get_all_todo(db)
    
    if response is None:
        raise Exception("Data not found")
    
    return {
        "status_code": 200,
        "description": "data found",
        "data": response
    }

@todo_router.put("/update/:id")
async def update_todo(request: Request):
    todo = request.json()
    id = int(request.path_params.get("id"))

    with sessionlocal as db:
        response = todo.update_todo_by_id(db, id, todo)
    
    if response is None:
        raise Exception("Cant update todo by this id")
    
    return {
        "status_code": 200,
        "description": "success updaet todo",
        "data": response
    }

@todo_router.delete("/delete/:id")
async def delete_todo_by_id(request: Request):
    id = int(request.path_params.get("id"))

    with sessionlocal as db:
        success = todo.delete_todo_by_id(db, id)
    
    if not success:
        raise Exception("Cant delete todo by this id")
    
    return {
        "status_code": 200,
        "description": "succes delete todo"
    }