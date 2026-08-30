from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import Transaction
from src.schemas import (
    TransactionCreate,
    TransactionUpdate,
)


class TransactionService:

    # ============================================================
    # Create Transaction
    # ============================================================

    def create(
        self,
        db: Session,
        user_id: int,
        data: TransactionCreate,
    ) -> Transaction:

        transaction = Transaction(
            user_id=user_id,
            category_id=data.category_id,
            amount=data.amount,
            transaction_type=data.transaction_type,
            description=data.description,
            transaction_date=data.transaction_date,
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    # ============================================================
    # Get User Transactions
    # ============================================================

    def get_all(
        self,
        db: Session,
        user_id: int,
    ) -> list[Transaction]:

        return list(
            db.scalars(
                select(Transaction)
                .where(
                    Transaction.user_id == user_id
                )
                .order_by(
                    Transaction.transaction_date.desc()
                )
            ).all()
        )

    # ============================================================
    # Get Transaction
    # ============================================================

    def get_by_id(
        self,
        db: Session,
        user_id: int,
        transaction_id: int,
    ) -> Transaction | None:

        return db.scalar(
            select(Transaction).where(
                Transaction.id == transaction_id,
                Transaction.user_id == user_id,
            )
        )

    # ============================================================
    # Update Transaction
    # ============================================================

    def update(
        self,
        db: Session,
        transaction: Transaction,
        data: TransactionUpdate,
    ) -> Transaction:

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(transaction, field, value)

        db.commit()
        db.refresh(transaction)

        return transaction

    # ============================================================
    # Delete Transaction
    # ============================================================

    def delete(
        self,
        db: Session,
        transaction: Transaction,
    ) -> None:

        db.delete(transaction)
        db.commit()


transaction_service = TransactionService()
