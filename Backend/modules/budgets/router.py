# ========================================
# Budget Router
# ========================================

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from modules.auth.dependencies import get_current_user
from modules.budgets.service import budget_service

from src.core.database import get_db
from src.models import User
from src.schemas import (
    BudgetCreate,
    BudgetResponse,
    BudgetUpdate,
)


# ========================================
# Router Configuration
# ========================================

router = APIRouter(
    prefix="/budgets",
    tags=["Budgets"],
)


# ========================================
# Create Budget
# ========================================

@router.post(
    "/",
    response_model=BudgetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_budget(
    data: BudgetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    return budget_service.create(
        db=db,
        user_id=current_user.id,
        data=data,
    )


# ========================================
# Get All Budgets
# ========================================

@router.get(
    "/",
    response_model=list[BudgetResponse],
)
def get_budgets(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    return budget_service.get_all(
        db=db,
        user_id=current_user.id,
    )


# ========================================
# Get Budget By ID
# ========================================

@router.get(
    "/{budget_id}",
    response_model=BudgetResponse,
)
def get_budget(
    budget_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    budget = budget_service.get_by_id(
        db=db,
        user_id=current_user.id,
        budget_id=budget_id,
    )

    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget not found",
        )

    return budget


# ========================================
# Update Budget
# ========================================

@router.patch(
    "/{budget_id}",
    response_model=BudgetResponse,
)
def update_budget(
    budget_id: int,
    data: BudgetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    budget = budget_service.get_by_id(
        db=db,
        user_id=current_user.id,
        budget_id=budget_id,
    )

    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget not found",
        )

    return budget_service.update(
        db=db,
        budget=budget,
        data=data,
    )


# ========================================
# Delete Budget
# ========================================

@router.delete(
    "/{budget_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_budget(
    budget_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    budget = budget_service.get_by_id(
        db=db,
        user_id=current_user.id,
        budget_id=budget_id,
    )

    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget not found",
        )

    budget_service.delete(
        db=db,
        budget=budget,
    )
