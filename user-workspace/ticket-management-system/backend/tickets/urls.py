from flask import Blueprint
from routes.ticket_routes import ticket_routes  # Corrigindo a importação do blueprint

tickets = Blueprint('tickets', __name__)

# Register ticket routes
tickets.register_blueprint(ticket_routes)
