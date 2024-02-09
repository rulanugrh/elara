from jose import JWTError, jwt
from . import hash
from config.config import *
from datetime import *

conf = GetConfig()

def verify_password(password, hash_password) -> str:
    return hash.ctx.verify(password, hash_password)

def create_access_token(data: dict, expires: timedelta = None):
    to_encode = data.copy()
    if expires:
        expire = datetime.utcnow() + expires
    else:
        expire =  datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, conf.APP_SECRET, "HS256")
    return encode_jwt

def decode_access_token(token: str):
    return jwt.decode(token, conf.APP_SECRET, "HS256")
