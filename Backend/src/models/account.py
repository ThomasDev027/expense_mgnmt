# ========================================
# Account Model
# ========================================

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    DateTime,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


# ========================================
# Type Checking Imports
# ========================================

if TYPE_CHECKING:
    from src.models.user import User


# ========================================
# Account Model
# ========================================

class Account(Base):
    __tablename__ = "accounts"

    # ----------------------------------------
    # Primary Key
    # ----------------------------------------

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    # ----------------------------------------
    # Account Name
    # ----------------------------------------

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # ----------------------------------------
    # Account Type
    # ----------------------------------------

    account_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    # ----------------------------------------
    # Account Balance
    # ----------------------------------------

    balance: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    # ----------------------------------------
    # Currency
    # ----------------------------------------

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR",
        nullable=False,
    )

    # ----------------------------------------
    # Description
    # ----------------------------------------

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ----------------------------------------
    # Status
    # ----------------------------------------

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ----------------------------------------
    # Timestamps
    # ----------------------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
