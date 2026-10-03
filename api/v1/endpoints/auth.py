from fastapi import APIRouter, HTTPException
from models import User, Role
from dependencies.database import db_dependency
from services.role_service import get_role_id
from schemas.auth import UserRegisterRequest, UserRegisterResponse
from schemas.shared import MessageResponse
from sqlalchemy import func
from core.security import hash_password

router = APIRouter(tags= ["Auth"])

@router.post("/register", response_model=MessageResponse)
async def register_user(request: UserRegisterRequest, db: db_dependency):

    user_exists = db.query(User).filter(func.lower(User.email) == request.email.casefold()).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="User Already Exists")

    new_user = User(
        username = request.username, 
        email = request.email,
        hash_password = hash_password(request.password),
        role_id = get_role_id(db, request.role),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Registered Successfully"}


@router.post("/login")
async def login():
    pass

@router.post("/logout")
async def logout():
    pass

@router.get("/me")
async def current_user():
    pass

@router.post("/refresh")
async def refresh_token():
    pass

