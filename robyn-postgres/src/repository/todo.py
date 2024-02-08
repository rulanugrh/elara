from model.todo import Todo
from sqlalchemy.orm import Session

def create_todo(db: Session, todo):
    data = Todo(**todo)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_todo_by_id(db: Session, id: int):
    return db.query(Todo).filter(Todo.id == id).first()

def get_all_todo(db: Session):
    return db.query(Todo).all()

def delete_todo_by_id(db: Session, id: int):
    data = get_todo_by_id(db, id)
    if data is None:
        return False

    db.delete(data)
    db.commit()

    return True

def update_todo_by_id(db: Session, id: int, todo):
    data = get_todo_by_id(db, id)
    if data is None:
        return False
    
    for i, res in todo.items():
        setattr(data, i, res)
    
    db.commit()
    db.refresh(data)

    return data