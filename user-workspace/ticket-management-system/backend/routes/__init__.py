from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)
department_routes = Blueprint('department_routes', __name__)
ticket_routes = Blueprint('ticket_routes', __name__)

# Importando as rotas
from .user_routes import *
from .department_routes import *
from .ticket_routes import *
