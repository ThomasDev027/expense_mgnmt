from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from modules.auth.dependencies import get_current_user
from src.models import User
from src.schemas import (
    ChangePasswordRequest,
    UpdateProfileRequest,
    UserResponse,
)
from modules.users.service import user_service
from src.core.database import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.put(
    "/me",
    response_model=UserResponse,
)
def update_my_profile(
    data: UpdateProfileRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return user_service.update_profile(
        db=db,
        user=current_user,
        data=data,
    )


@router.put(
    "/me/password",
    status_code=status.HTTP_204_NO_CONTENT,
)
def change_my_password(
    data: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        user_service.change_password(
            db=db,
            user=current_user,
            current_password=data.current_password,
            new_password=data.new_password,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

    return None
