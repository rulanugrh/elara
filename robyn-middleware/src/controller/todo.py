from robyn import SubRouter
from robyn.authentication import BearerGetter
from repository import todo
from config.config import GetConnection

todo_router = SubRouter(__name__, prefix="/api/v1/todo")
sessionlocal = GetConnection()
todo_router.configure_authentication(verify.BasicAuthHandler(token_getter=BearerGetter()))

@todo_router.post("/create")
async def create_todo(request):
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
async def get_todo_by_id(request):
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
async def get_all_todo(request):
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
async def update_todo(request):
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
async def delete_todo_by_id(request):
    id = int(request.path_params.get("id"))

    with sessionlocal as db:
        success = todo.delete_todo_by_id(db, id)
    
    if not success:
        raise Exception("Cant delete todo by this id")
    
    return {
        "status_code": 200,
        "description": "succes delete todo"
    }