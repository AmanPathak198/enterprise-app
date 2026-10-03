# id, name, resource, action, description
from db.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
class Permission(Base):
    __tablename__ = "permissions"
    id =Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    resource = Column(String(50), nullable=False)
    action = Column(String(50), nullable=False)
    description = Column(String, nullable=True)
    role_permissions = relationship(
        "RolePermission", back_populates="permission",
        cascade="all, delete-orphan"
    )