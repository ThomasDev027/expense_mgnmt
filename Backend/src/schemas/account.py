# ========================================
# Account Schemas
# ========================================

from decimal import Decimal

from pydantic import BaseModel, Field


# ========================================
# Create Account
# ========================================

class AccountCreate(BaseModel):

    name: str = Field(
        min_length=1,
        max_length=100,
    )

    account_type: str = Field(
        max_length=30,
    )

    balance: Decimal = Field(
        default=0,
        ge=0,
    )

    currency: str = Field(
        default="INR",
        max_length=10,
    )

    description: str | None = None


# ========================================
# Update Account
# ========================================

class AccountUpdate(BaseModel):

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    account_type: str | None = Field(
        default=None,
        max_length=30,
    )

    balance: Decimal | None = Field(
        default=None,
        ge=0,
    )

    currency: str | None = Field(
        default=None,
        max_length=10,
    )

    description: str | None = None

    is_active: bool | None = None


# ========================================
# Account Response
# ========================================

class AccountResponse(BaseModel):

    id: int
    user_id: int
    name: str
    account_type: str
    balance: Decimal
    currency: str
    description: str | None
    is_active: bool

    model_config = {
        "from_attributes": True,
    }
