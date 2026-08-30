from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.core.exceptions import UnauthorizedException
from src.core.security import decode_access_token
from src.models import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:

    try:
        payload = decode_access_token(token)

        user_id = payload.get("sub")

        if not user_id:
            raise UnauthorizedException(
                "Invalid authentication token"
            )

        user = db.scalar(
            select(User).where(
                User.id == int(user_id)
            )
        )

    except (JWTError, ValueError):
        raise UnauthorizedException(
            "Invalid authentication token"
        )

    if not user:
        raise UnauthorizedException(
            "User not found"
        )

    if not user.is_active:
        raise UnauthorizedException(
            "User account is inactive"
        )

    return user
