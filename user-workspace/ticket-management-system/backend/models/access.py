from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class DepartmentAccess(Base):
    __tablename__ = 'department_access'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    user = relationship("User", back_populates="department_access")
    department = relationship("Department", back_populates="department_access")

def __repr__(self):
    return f'<DepartmentAccess user_id={self.user_id}, department_id={self.department_id}>'
