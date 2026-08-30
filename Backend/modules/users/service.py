from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import User
from src.schemas import UpdateProfileRequest
from src.core.security import hash_password, verify_password


class UserService:

    def get_by_id(
        self,
        db: Session,
        user_id: int,
    ) -> User | None:

        return db.scalar(
            select(User).where(
                User.id == user_id,
            )
        )

    def update_profile(
        self,
        db: Session,
        user: User,
        data: UpdateProfileRequest,
    ) -> User:

        if data.full_name is not None:
            user.full_name = data.full_name

        # if data.email is not None:
        #     user.email = data.email

        db.commit()
        db.refresh(user)

        return user

    def change_password(
        self,
        db: Session,
        user: User,
        current_password: str,
        new_password: str,
    ) -> None:

        if not verify_password(
            current_password,
            user.password_hash,
        ):
            raise ValueError(
                "Current password is incorrect"
            )

        user.password_hash = hash_password(
            new_password
        )

        db.commit()


user_service = UserService()
