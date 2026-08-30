# ========================================
# Transaction Model
# ========================================

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Numeric,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.core.database import Base


# ========================================
# Type Checking Imports
# ========================================

if TYPE_CHECKING:
    from src.models.user import User
    from src.models.transaction_type import TransactionType


# ========================================
# Transaction Model
# ========================================

class Transaction(Base):
    __tablename__ = "transactions"

    # ============================================================
    # Primary Key
    # ============================================================

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    # ============================================================
    # Foreign Keys
    # ============================================================

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    transaction_type_id: Mapped[int] = mapped_column(
        ForeignKey(
            "transaction_types.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    # ============================================================
    # Transaction Information
    # ============================================================

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    transaction_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    # ============================================================
    # Timestamps
    # ============================================================

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

    # ============================================================
    # User Relationship
    # ============================================================

    user: Mapped["User"] = relationship(
        "User",
        back_populates="transactions",
    )

    # ============================================================
    # Transaction Type Relationship
    # ============================================================

    transaction_type: Mapped["TransactionType"] = relationship(
        "TransactionType",
        back_populates="transactions",
    )

