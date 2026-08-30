from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.auth.dependencies import get_current_user
from modules.categories.service import category_service

from src.core.database import get_db
from src.models import User
from src.schemas import CategoryResponse


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get(
    "/",
    response_model=list[CategoryResponse],
)
def get_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return category_service.get_categories(
        db=db,
    )
