# ========================================
# Account Service
# ========================================

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import Account
from src.schemas import (
    AccountCreate,
    AccountUpdate,
)


# ========================================
# Account Service Class
# ========================================

class AccountService:

    # ----------------------------------------
    # Create Account
    # ----------------------------------------

    def create(
        self,
        db: Session,
        user_id: int,
        data: AccountCreate,
    ) -> Account:

        account = Account(
            user_id=user_id,
            name=data.name,
            account_type=data.account_type,
            balance=data.balance,
            currency=data.currency,
            description=data.description,
        )

        db.add(account)
        db.commit()
        db.refresh(account)

        return account

    # ----------------------------------------
    # Get All Accounts
    # ----------------------------------------

    def get_all(
        self,
        db: Session,
        user_id: int,
    ) -> list[Account]:

        return list(
            db.scalars(
                select(Account)
                .where(
                    Account.user_id == user_id,
                    Account.is_active.is_(True),
                )
                .order_by(
                    Account.name
                )
            ).all()
        )

    # ----------------------------------------
    # Get Account By ID
    # ----------------------------------------

    def get_by_id(
        self,
        db: Session,
        user_id: int,
        account_id: int,
    ) -> Account | None:

        return db.scalar(
            select(Account).where(
                Account.id == account_id,
                Account.user_id == user_id,
            )
        )

    # ----------------------------------------
    # Update Account
    # ----------------------------------------

    def update(
        self,
        db: Session,
        account: Account,
        data: AccountUpdate,
    ) -> Account:

        update_data = data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                account,
                field,
                value,
            )

        db.commit()
        db.refresh(account)

        return account

    # ----------------------------------------
    # Delete Account
    # ----------------------------------------

    def delete(
        self,
        db: Session,
        account: Account,
    ) -> None:

        # Soft delete
        account.is_active = False

        db.commit()


# ========================================
# Account Service Instance
# ========================================

account_service = AccountService()
