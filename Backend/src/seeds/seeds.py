# ========================================
# Database Seeds
# ========================================

from src.core.database import SessionLocal

from src.seeds.accounts import seed_accounts
from src.seeds.categories import seed_categories
from src.seeds.roles import seed_roles
from src.seeds.transaction_types import seed_transaction_categories


# ========================================
# Run All Seeds
# ========================================

def run_seeds() -> None:
    session = SessionLocal()

    try:
        # ----------------------------------------
        # Seed Roles
        # ----------------------------------------

        seed_roles(session)

        # ----------------------------------------
        # Seed Categories
        # ----------------------------------------

        seed_categories(session)

        # ----------------------------------------
        # Seed Accounts
        # ----------------------------------------

        seed_accounts(session)

        # ----------------------------------------
        # Seed Transaction Categories & Types
        # ----------------------------------------

        seed_transaction_categories(session)

        # ----------------------------------------
        # Commit All Seeds
        # ----------------------------------------

        session.commit()

        print("Database seeds completed successfully.")

    except Exception:
        # ----------------------------------------
        # Rollback on Error
        # ----------------------------------------

        session.rollback()

        print("Database seeding failed. Changes rolled back.")

        raise

    finally:
        # ----------------------------------------
        # Close Database Session
        # ----------------------------------------

        session.close()


# ========================================
# Entry Point
# ========================================

if __name__ == "__main__":
    run_seeds()
