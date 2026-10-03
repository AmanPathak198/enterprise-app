from dependencies.database import db_dependency
from models.role import Role
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException


def get_role_id(db: Session, role_name: str)-> int:
    role = db.query(Role).filter(func.lower(Role.name) == role_name.casefold()).first()
    if not role:
        raise HTTPException(status_code=400, detail="Invalid role")
    return role.id
