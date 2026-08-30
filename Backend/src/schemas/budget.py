# ========================================
# Budget Schemas
# ========================================

from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


# ========================================
# Create Budget
# ========================================

class BudgetCreate(BaseModel):

    category_id: int

    amount: Decimal = Field(
        gt=0,
    )

    period: str = Field(
        default="monthly",
        max_length=20,
    )

    start_date: date

    end_date: date


# ========================================
# Update Budget
# ========================================

class BudgetUpdate(BaseModel):

    category_id: int | None = None

    amount: Decimal | None = Field(
        default=None,
        gt=0,
    )

    period: str | None = Field(
        default=None,
        max_length=20,
    )

    start_date: date | None = None

    end_date: date | None = None

    is_active: bool | None = None


# ========================================
# Budget Response
# ========================================

class BudgetResponse(BaseModel):

    id: int
    user_id: int
    category_id: int
    amount: Decimal
    period: str
    start_date: date
    end_date: date
    is_active: bool

    model_config = {
        "from_attributes": True,
    }
