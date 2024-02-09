from sqlalchemy.orm import Session
from model import User
from middleware import jwt, hash

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, req: User):
    hashed_password = hash_password(req.password)
    data = User(email=req.email, name=req.name, password=hashed_password)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user is None:
        return False
    if not jwt.verify_password(password, user.password):
        return False
    
    create_token = jwt.create_access_token(data={"id": user.id,"name": user.name})
    return create_token