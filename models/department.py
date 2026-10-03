from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from db.base import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String(200), nullable=True)
    manager_id = Column(Integer, ForeignKey("employees.id"), nullable=True )
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    employees = relationship(
        "Employee", back_populates="department",
        foreign_keys="Employee.department_id"
    )
    manager = relationship(
        "Employee", foreign_keys=[manager_id],
        post_update=True
    )
