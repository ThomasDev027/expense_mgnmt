# ========================================
# Account Router
# ========================================

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from modules.auth.dependencies import get_current_user
from modules.accounts.service import account_service

from src.core.database import get_db
from src.models import User
from src.schemas import (
    AccountCreate,
    AccountResponse,
    AccountUpdate,
)


# ========================================
# Router Configuration
# ========================================

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)

# ========================================
# Get All Accounts
# ========================================

@router.get(
    "/",
    response_model=list[AccountResponse],
)
def get_accounts(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    return account_service.get_all(
        db=db,
        user_id=current_user.id,
    )


# ========================================
# Create Account
# ========================================

@router.post(
    "/",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_account(
    data: AccountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    return account_service.create(
        db=db,
        user_id=current_user.id,
        data=data,
    )



# ========================================
# Get Account By ID
# ========================================

@router.get(
    "/{account_id}",
    response_model=AccountResponse,
)
def get_account(
    account_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    account = account_service.get_by_id(
        db=db,
        user_id=current_user.id,
        account_id=account_id,
    )

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )

    return account


# ========================================
# Update Account
# ========================================

@router.patch(
    "/{account_id}",
    response_model=AccountResponse,
)
def update_account(
    account_id: int,
    data: AccountUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    account = account_service.get_by_id(
        db=db,
        user_id=current_user.id,
        account_id=account_id,
    )

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )

    return account_service.update(
        db=db,
        account=account,
        data=data,
    )


# ========================================
# Delete Account
# ========================================

@router.delete(
    "/{account_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_account(
    account_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    account = account_service.get_by_id(
        db=db,
        user_id=current_user.id,
        account_id=account_id,
    )

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )

    account_service.delete(
        db=db,
        account=account,
    )
