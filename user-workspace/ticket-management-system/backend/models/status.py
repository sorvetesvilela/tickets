from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)  # Associando status a departamentos

    department = relationship("Department", back_populates="statuses")  # Relação com o departamento

    def __repr__(self):
        return f'<Status {self.name}>'
