from pydantic import BaseModel, EmailStr, Field
from docs.users_docs import user_fields, user_example

class UserCreate(BaseModel):
    name: str = Field(..., description=user_fields["name"])
    email: EmailStr = Field(..., description=user_fields["email"])
    age: int = Field(..., gt=0, description=user_fields["age"])

    class Config:
        schema_extra = {"example": user_example}