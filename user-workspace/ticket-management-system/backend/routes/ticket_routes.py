from flask import request, jsonify
from . import ticket_routes
from models.ticket import Ticket

@ticket_routes.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = Ticket(title=data['title'], description=data['description'], status_id=data['status_id'], department_id=data['department_id'])
    # Add logic to save the ticket to the database
    return jsonify({'message': 'Ticket created successfully'}), 201

@ticket_routes.route('/tickets', methods=['GET'])
def get_tickets():
    # Add logic to retrieve all tickets from the database
    return jsonify(tickets), 200
