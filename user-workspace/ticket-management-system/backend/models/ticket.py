from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    status = relationship("Status", back_populates="tickets")
    department = relationship("Department", back_populates="tickets")

    def __repr__(self):
        return f'<Ticket {self.title}>'
