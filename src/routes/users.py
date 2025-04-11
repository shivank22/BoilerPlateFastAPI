from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, EmailStr, Field
from fastapi.responses import JSONResponse
# from auth.azure_auth import verify_azure_identity
from docs.users_docs import user_create_summary, user_create_description, user_fields, user_example

router = APIRouter(prefix="/users", tags=["Users"])# dependencies=[Depends(verify_azure_identity)]

class UserCreate(BaseModel):
    name: str = Field(..., description=user_fields["name"])
    email: EmailStr = Field(..., description=user_fields["email"])
    age: int = Field(..., gt=0, description=user_fields["age"])

    class Config:
        schema_extra = {"example": user_example}

@router.post("/", summary=user_create_summary, description=user_create_description)
def create_user(user: UserCreate):
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User created", "user": user.dict()})