# ========================================
# Account Seed
# ========================================

from sqlalchemy import select

from src.models.account import Account
from sqlalchemy.orm import Session

# ========================================
# Seed Accounts
# ========================================

def seed_accounts(session: Session) -> None:

    try:
        # ----------------------------------------
        # Default Accounts
        # ----------------------------------------

        accounts = [
            {
                "name": "Cash",
                "account_type": "cash",
                "balance": 0,
                "currency": "INR",
                "description": "Physical cash",
            },
            {
                "name": "Bank Account",
                "account_type": "bank",
                "balance": 0,
                "currency": "INR",
                "description": "Primary bank account",
            },
            {
                "name": "Credit Card",
                "account_type": "credit_card",
                "balance": 0,
                "currency": "INR",
                "description": "Credit card account",
            },
            {
                "name": "Wallet",
                "account_type": "wallet",
                "balance": 0,
                "currency": "INR",
                "description": "Digital wallet",
            },
        ]

        # ----------------------------------------
        # Create Default Accounts
        # ----------------------------------------

        for account_data in accounts:

            existing_account = session.scalar(
                select(Account).where(
                    Account.name == account_data["name"],
                )
            )

            if existing_account:
                continue

            account = Account(
                name=account_data["name"],
                account_type=account_data["account_type"],
                balance=account_data["balance"],
                currency=account_data["currency"],
                description=account_data["description"],
                is_active=True,
            )

            session.add(account)

        # ----------------------------------------
        # Save Changes
        # ----------------------------------------

        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


# ========================================
# Run Seed
# ========================================

if __name__ == "__main__":
    seed_accounts()
