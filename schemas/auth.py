from pydantic import BaseModel, fields, EmailStr, Field
from typing import Literal, Annotated, Optional
from pydantic import StringConstraints
from datetime import datetime

class UserRegisterRequest(BaseModel):
    username: Annotated[str, StringConstraints(strip_whitespace=True, min_length=3, max_length= 25)] = Field(..., examples =["aman123"])
    email: EmailStr = Field(..., examples= ["aman@email.com"])
    password: Annotated[str, StringConstraints(min_length=8, max_length=128)]= Field(..., examples=["StrongPass!23"])
    role: Literal["SuperAdmin", "Admin", "Manager", "Employee", "Print Operator"] = "Employee"
    class Config:
        orm_mode = True

class UserRegisterResponse(BaseModel):
    id: str
    username:str
    email: EmailStr
    role: Literal["SuperAdmin", "Admin","Manager", "Employee", "Print Operator"]
    is_active: bool
    is_verified: bool
    created_at: datetime
    last_login_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=128)]
