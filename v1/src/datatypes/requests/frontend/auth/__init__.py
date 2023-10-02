from pydantic import BaseModel, EmailStr
from fastapi import Query

from v1.config import password_min_length, password_max_length


class Login(BaseModel):
    email: EmailStr
    password: str = Query(
        min_length=password_min_length,
        max_length=password_max_length
    )
