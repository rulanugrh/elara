from passlib.context import CryptContext

ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return ctx.hash(password)