from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.ticket import Ticket  # Ajuste o caminho conforme necessário
from models.status import Status  # Importar a classe Status
from models.department import Department  # Importar a classe Department
from database import Base  # Ajuste o caminho conforme necessário

# Configuração do banco de dados
DATABASE_URL = "sqlite:///ticket_management.db"  # Altere para o seu banco de dados
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Teste de criação
new_ticket = Ticket(title="Teste de Ticket", description="Descrição do ticket", status_id=1, department_id=1)
session.add(new_ticket)
session.commit()

# Teste de leitura
ticket = session.query(Ticket).first()
print(ticket)

# Teste de atualização
ticket.title = "Título Atualizado"
session.commit()

# Teste de exclusão
session.delete(ticket)
session.commit()

# Fechar a sessão
session.close()
