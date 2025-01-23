from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Corrigindo a importação

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    status = relationship("Status")
    department = relationship("Department")

    def __repr__(self):
        return f'<Ticket {self.title}>'
