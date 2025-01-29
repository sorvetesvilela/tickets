{
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.orm import relationship
    from database import Base
    from .access import DepartmentAccess  # Importando o modelo de controle de acesso

    class Department(Base):
        __tablename__ = 'departments'

        id = Column(Integer, primary_key=True)
        name = Column(String(100), unique=True, nullable=False)

        tickets = relationship("Ticket", back_populates="department")
        department_access = relationship("DepartmentAccess", back_populates="department")  # Relação com o controle de acesso

    def __repr__(self):
        return f'<Department {self.name}>'
}
</create_file>
