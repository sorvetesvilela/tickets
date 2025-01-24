from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status_id = Column(Integer, ForeignKey('statuses.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))

    status = relationship("Status", back_populates="tickets")
    department = relationship("Department", back_populates="tickets")
