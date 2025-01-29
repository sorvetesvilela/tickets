from flask import request, jsonify
from flask_jwt_extended import jwt_required
from database import SessionLocal
from marshmallow import Schema, fields, ValidationError

class TicketSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    status_id = fields.Int(required=True)
    department_id = fields.Int(required=True)
from models.ticket import Ticket
from models.status import Status
from models.department import Department
from . import ticket_routes

@ticket_routes.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()  
    # Validate the incoming data
    try:
        TicketSchema().load(data)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    db = SessionLocal()
    try:
        new_ticket = Ticket(title=data['title'], description=data['description'], status_id=data['status_id'], department_id=data['department_id'])
        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)
        return jsonify({'message': 'Ticket created successfully', 'ticket_id': new_ticket.id}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@ticket_routes.route('/tickets', methods=['GET'])
def get_tickets():
    db = SessionLocal()
    try:
        tickets = db.query(Ticket).all()
        return jsonify([{'id': ticket.id, 'title': ticket.title, 'description': ticket.description} for ticket in tickets]), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@ticket_routes.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.get_json()  
    # Validate the incoming data
    try:
        TicketSchema().load(data)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    db = SessionLocal()
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            return jsonify({'error': 'Ticket not found'}), 404
        
        ticket.title = data.get('title', ticket.title)
        ticket.description = data.get('description', ticket.description)
        ticket.status_id = data.get('status_id', ticket.status_id)
        ticket.department_id = data.get('department_id', ticket.department_id)
        
        db.commit()
        return jsonify({'message': 'Ticket updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@ticket_routes.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    db = SessionLocal()
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            return jsonify({'error': 'Ticket not found'}), 404
        
        db.delete(ticket)
        db.commit()
        return jsonify({'message': 'Ticket deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()
