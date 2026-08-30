# ========================================
# Category Model
# ========================================

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


# ========================================
# Type Checking Imports
# ========================================

if TYPE_CHECKING:
    from src.models.budget import Budget


# ========================================
# Category Model
# ========================================

class Categories(Base):
    __tablename__ = "categories"

    # ============================================================
    # Primary Key
    # ============================================================

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    # ============================================================
    # Category Details
    # ============================================================

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
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
    # Timestamp
    # ============================================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )

    # ============================================================
    # Budget Relationship
    # ============================================================

    budgets: Mapped[list["Budget"]] = relationship(
        "Budget",
        back_populates="categories",
    )