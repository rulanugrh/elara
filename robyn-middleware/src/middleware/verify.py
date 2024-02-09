from robyn.authentication import AuthenticationHandler, BearerGetter, Identity
from . import jwt
from config import config
from repository import user

sessionlocal = config.GetConnection()

class BasicAuthHandler(AuthenticationHandler):
    def authenticate(self, request):
        token = self.token_getter.get_token(request)
        try:
            payload = jwt.decode_access_token(token)
            id = payload["id"]
            name = payload["name"]

        except Exception:
            return False
        
        with sessionlocal as db:
            data = user.get_user_by_name(db, name)
        
        return Identity(claims={"user": f"{data}"})
