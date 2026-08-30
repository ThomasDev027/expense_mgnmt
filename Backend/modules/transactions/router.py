from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from modules.auth.dependencies import get_current_user
from src.core.database import get_db
from src.models import User
from src.schemas import (
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate,
)

from modules.transactions.service import transaction_service


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

# ================================================================
# Get My Transactions
# ================================================================

@router.get(
    "/",
    response_model=list[TransactionResponse],
)
def get_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return transaction_service.get_all(
        db=db,
        user_id=current_user.id,
    )


# ================================================================
# Create Transaction
# ================================================================

@router.post(
    "/",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return transaction_service.create(
        db=db,
        user_id=current_user.id,
        data=data,
    )



# ================================================================
# Get Transaction
# ================================================================

@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse,
)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transaction = transaction_service.get_by_id(
        db=db,
        user_id=current_user.id,
        transaction_id=transaction_id,
    )

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )

    return transaction


# ================================================================
# Update Transaction
# ================================================================

@router.patch(
    "/{transaction_id}",
    response_model=TransactionResponse,
)
def update_transaction(
    transaction_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transaction = transaction_service.get_by_id(
        db=db,
        user_id=current_user.id,
        transaction_id=transaction_id,
    )

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )

    return transaction_service.update(
        db=db,
        transaction=transaction,
        data=data,
    )


# ================================================================
# Delete Transaction
# ================================================================

@router.delete(
    "/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transaction = transaction_service.get_by_id(
        db=db,
        user_id=current_user.id,
        transaction_id=transaction_id,
    )

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )

    transaction_service.delete(
        db=db,
        transaction=transaction,
    )

    return None
