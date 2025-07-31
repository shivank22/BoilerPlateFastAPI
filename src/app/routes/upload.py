from fastapi import APIRouter, UploadFile, File, Depends
from src.app.auth.dependencies import get_current_user

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    return {"message": f"File received from user {current_user}"}
