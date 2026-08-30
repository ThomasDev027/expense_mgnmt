from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


# ============================================================
# Transaction Create
# ============================================================

class TransactionCreate(BaseModel):
    category_id: int

    amount: Decimal = Field(
        gt=0,
        max_digits=12,
        decimal_places=2,
    )

    transaction_type: str = Field(
        min_length=1,
        max_length=20,
    )

    description: str | None = None

    transaction_date: datetime


# ============================================================
# Transaction Update
# ============================================================

class TransactionUpdate(BaseModel):
    category_id: int | None = None

    amount: Decimal | None = Field(
        default=None,
        gt=0,
        max_digits=12,
        decimal_places=2,
    )

    transaction_type: str | None = Field(
        default=None,
        min_length=1,
        max_length=20,
    )

    description: str | None = None

    transaction_date: datetime | None = None


# ============================================================
# Transaction Response
# ============================================================

class TransactionResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    user_id: int
    category_id: int
    amount: Decimal
    transaction_type: str
    description: str | None
    transaction_date: datetime
    created_at: datetime
    updated_at: datetime
