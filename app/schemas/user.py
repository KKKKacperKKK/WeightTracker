from decimal import Decimal

from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict


class UserRegister(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)
    height: Decimal = Field(ge=130, le=230)

    @field_validator("password")
    @classmethod
    def password_validator(cls, password: str) -> str:
        bytes_password = password.encode("utf-8")
        if len(bytes_password) > 72:
            raise ValueError("Password too long!")
        return password


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: EmailStr
    height: Decimal


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"    