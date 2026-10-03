from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from db.base import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    employee_code = Column(String(30), nullable= False, unique=True )
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    phone = Column(String(15), nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    designation = Column(String(30),nullable= True )
    joining_date = Column(DateTime, nullable=True)
    salary = Column(DECIMAL(12, 2), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))
    user = relationship("User", back_populates="employee")
    department = relationship(
        "Department", back_populates="employees",
        foreign_keys=[department_id]
    )
