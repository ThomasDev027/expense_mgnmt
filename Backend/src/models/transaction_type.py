# ========================================
# Transaction Type Model
# ========================================

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


if TYPE_CHECKING:
    from src.models.transaction import Transaction
    from src.models.transaction_category import TransactionCategory


class TransactionType(Base):
    __tablename__ = "transaction_types"

    # ============================================================
    # Primary Key
    # ============================================================

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    # ============================================================
    # Category Foreign Key
    # ============================================================

    category_id: Mapped[int] = mapped_column(
        ForeignKey(
            "transaction_categories.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ============================================================
    # Type Information
    # ============================================================

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ============================================================
    # Status
    # ============================================================

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ============================================================
    # Category Relationship
    # ============================================================

    category: Mapped["TransactionCategory"] = relationship(
        "TransactionCategory",
        back_populates="transaction_types",
    )

    # ============================================================
    # Transactions Relationship
    # ============================================================

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="transaction_type",
    )
