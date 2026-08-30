from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import User, Role

from src.schemas import (
    LoginRequest,
    RegisterRequest,
)

from src.core.exceptions import (
    ConflictException,
    UnauthorizedException,
)

from src.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)


class AuthService:

    def register(
        self,
        db: Session,
        data: RegisterRequest,
    ) -> User:

        email = data.email.lower()

        existing_user = db.scalar(
            select(User).where(
                User.email == email
            )
        )

        if existing_user:
            raise ConflictException(
                "Email is already registered"
            )

        # Get default user role
        role = db.scalar(
            select(Role).where(
                Role.name == "user"
            )
        )

        if not role:
            raise Exception(
                "Default user role not found"
            )

        user = User(
            email=email,
            password_hash=hash_password(
                data.password
            ),
            full_name=data.full_name,
            role_id=role.id,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def authenticate(
        self,
        db: Session,
        data: LoginRequest,
    ) -> str:

        email = data.email.lower()

        user = db.scalar(
            select(User).where(
                User.email == email
            )
        )

        if not user:
            raise UnauthorizedException(
                "Invalid email or password"
            )

        if not verify_password(
            data.password,
            user.password_hash,
        ):
            raise UnauthorizedException(
                "Invalid email or password"
            )

        if not user.is_active:
            raise UnauthorizedException(
                "User account is inactive"
            )

        return create_access_token(
            user_id=user.id,
            role=user.role.name,
        )


auth_service = AuthService()