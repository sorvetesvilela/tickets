from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    tickets = relationship("Ticket", back_populates="department")

def __repr__(self):
        return f'<Department {self.name}>'
