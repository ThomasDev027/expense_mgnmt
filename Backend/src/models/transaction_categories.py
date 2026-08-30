# ========================================
# Transaction Category Model
# ========================================

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


if TYPE_CHECKING:
    from src.models.transaction_type import TransactionType


class TransactionCategory(Base):
    __tablename__ = "transaction_categories"

    # ============================================================
    # Primary Key
    # ============================================================

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    # ============================================================
    # Category Information
    # ============================================================

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
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
    # Transaction Types
    # ============================================================

    transaction_types: Mapped[list["TransactionType"]] = relationship(
        "TransactionType",
        back_populates="category",
        cascade="all, delete-orphan",
    )
