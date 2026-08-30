from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    # role_id: int


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    role_id: int
    is_active: bool
    created_at: datetime


class UpdateProfileRequest(BaseModel):
    full_name: str | None = None