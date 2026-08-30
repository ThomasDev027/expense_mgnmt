# ========================================
# Budget Service
# ========================================

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import Budget
from src.schemas import BudgetCreate, BudgetUpdate


# ========================================
# Budget Service Class
# ========================================

class BudgetService:

    # ----------------------------------------
    # Create Budget
    # ----------------------------------------

    def create(
        self,
        db: Session,
        user_id: int,
        data: BudgetCreate,
    ) -> Budget:

        budget = Budget(
            user_id=user_id,
            category_id=data.category_id,
            amount=data.amount,
            period=data.period,
            start_date=data.start_date,
            end_date=data.end_date,
        )

        db.add(budget)
        db.commit()
        db.refresh(budget)

        return budget

    # ----------------------------------------
    # Get All Budgets
    # ----------------------------------------

    def get_all(
        self,
        db: Session,
        user_id: int,
    ) -> list[Budget]:

        return list(
            db.scalars(
                select(Budget)
                .where(
                    Budget.user_id == user_id,
                    Budget.is_active.is_(True),
                )
                .order_by(
                    Budget.start_date.desc()
                )
            ).all()
        )

    # ----------------------------------------
    # Get Budget By ID
    # ----------------------------------------

    def get_by_id(
        self,
        db: Session,
        user_id: int,
        budget_id: int,
    ) -> Budget | None:

        return db.scalar(
            select(Budget).where(
                Budget.id == budget_id,
                Budget.user_id == user_id,
            )
        )

    # ----------------------------------------
    # Update Budget
    # ----------------------------------------

    def update(
        self,
        db: Session,
        budget: Budget,
        data: BudgetUpdate,
    ) -> Budget:

        update_data = data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                budget,
                field,
                value,
            )

        db.commit()
        db.refresh(budget)

        return budget

    # ----------------------------------------
    # Delete Budget
    # ----------------------------------------

    def delete(
        self,
        db: Session,
        budget: Budget,
    ) -> None:

        # Soft delete
        budget.is_active = False

        db.commit()


# ========================================
# Budget Service Instance
# ========================================

budget_service = BudgetService()
