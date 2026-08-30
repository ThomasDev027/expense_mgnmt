# ========================================
# Budget Model
# ========================================

from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


# ========================================
# Type Checking Imports
# ========================================

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.categories import Categories


# ========================================
# Budget Model
# ========================================

class Budget(Base):
    __tablename__ = "budgets"

    # ----------------------------------------
    # Primary Key
    # ----------------------------------------

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    # ----------------------------------------
    # User
    # ----------------------------------------

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # ----------------------------------------
    # Category
    # ----------------------------------------

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
        index=True,
    )

    # ----------------------------------------
    # Budget Amount
    # ----------------------------------------

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    # ----------------------------------------
    # Budget Period
    # ----------------------------------------

    period: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    # ----------------------------------------
    # Budget Dates
    # ----------------------------------------

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
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

    # ----------------------------------------
    # Relationships
    # ----------------------------------------

    user: Mapped["User"] = relationship(
        "User",
        back_populates="budgets",
    )

    categories: Mapped["Categories"] = relationship(
        "Categories",
        back_populates="budgets",
    )


