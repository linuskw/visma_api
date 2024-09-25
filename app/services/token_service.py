from datetime import datetime, timedelta
import jwt
from jwt import ExpiredSignatureError
from flask import abort

class TokenService:
    SECRET_KEY = "Top Secret Key!!!"

    @staticmethod
    def create_user_token(user: dict):

        token_json = {
            "exp": datetime.utcnow() + timedelta(minutes=60),
            "u_id": str(user["_id"]),
            "u_name": user["username"],
        }

        token = TokenService._encode_token(token_json)
        return {
            'token': token,
        }, 200

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(
                token,
                TokenService.SECRET_KEY,
                algorithm='HS256',
            )

        except ExpiredSignatureError as e:
            abort(401, {"message": "Token expired"})
        except Exception as e:
            abort(401, {"message": "Invalid Token"})

    @staticmethod
    def _encode_token(token_json):
        return jwt.encode(token_json, TokenService.SECRET_KEY, algorithm='HS256').decode("utf-8")
