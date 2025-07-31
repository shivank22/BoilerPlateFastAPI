from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.app.models.user import User
from src.app.models.base import get_session, init_db
from src.app.schemas.auth import LoginRequest, LoginResponse
from src.app.auth.utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])
init_db()

@router.post("/register", response_model=LoginResponse)
def register(data: LoginRequest, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.username == data.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(username=data.username, hashed_password=hash_password(data.password))
    session.add(user)
    session.commit()
    session.refresh(user)

    token = create_access_token({"sub": user.username})
    return {"message": "User created successfully", "token": token}

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == data.username)).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": user.username})
    return {"message": "Login successful", "token": token}
