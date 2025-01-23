from database import engine, Base
from models.user import User
from models.department import Department
from models.ticket import Ticket
from models.status import Status  # Adicionando a importação do modelo Status

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized and tables created.")
