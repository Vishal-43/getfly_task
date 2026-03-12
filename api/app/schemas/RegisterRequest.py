from pydantic import BaseModel, EmailStr
from typing import Optional




class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: Optional[str] = None