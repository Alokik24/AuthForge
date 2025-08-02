from pydantic import BaseModel, EmailStr, Field

# User registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str = None

# User login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#  JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str

# User response model
class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    is_active: bool
    is_verified: bool

    class Config:
        from_attributes = True # allows models to use attributes from the ORM model 