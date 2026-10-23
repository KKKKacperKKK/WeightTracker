from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from app.config.settings import settings
from app.core.exceptions import InvalidAccessToken


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    return hashed_bytes.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_bytes, hashed_bytes)


def create_access_token(user_id: int) -> str:
    time_now = datetime.now(timezone.utc)
    token_lifetime = timedelta(minutes=settings.access_token_expire_minutes)
    payload = {
        "sub": str(user_id),
        "exp": time_now + token_lifetime,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> int:
    try:
        decoded_jwt = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        return int(decoded_jwt["sub"])
    except jwt.InvalidTokenError:
        raise InvalidAccessToken()