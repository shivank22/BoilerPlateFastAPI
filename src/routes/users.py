from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from auth.azure_auth import verify_azure_identity
from docs.users_docs import user_metadata
from schemas.user import UserCreate

router = APIRouter(prefix="/users", tags=["Users"],dependencies=[Depends(verify_azure_identity)])

@router.post("/", summary=user_metadata.Create.summary, description=user_metadata.Create.description)
def create_user(user: UserCreate):
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User created", "user": user.dict()})