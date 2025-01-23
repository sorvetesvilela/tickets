from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    # Adding a relationship to Ticket
    tickets = relationship("Ticket", back_populates="status")

    def __repr__(self):
        return f'<Status {self.name}>'
