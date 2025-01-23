from flask import Blueprint, request, jsonify
from models.status import Status
from database import SessionLocal

status_routes = Blueprint('status_routes', __name__)  # Definindo o blueprint

@status_routes.route('/statuses', methods=['POST'])
def create_status():
    data = request.get_json()
    db = SessionLocal()
    try:
        new_status = Status(name=data['name'])
        db.add(new_status)
        db.commit()
        db.refresh(new_status)
        return jsonify({'message': 'Status created successfully', 'status_id': new_status.id}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@status_routes.route('/statuses', methods=['GET'])
def get_statuses():
    db = SessionLocal()
    try:
        statuses = db.query(Status).all()
        return jsonify([{'id': status.id, 'name': status.name} for status in statuses]), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@status_routes.route('/statuses/<int:status_id>', methods=['PUT'])
def update_status(status_id):
    data = request.get_json()
    db = SessionLocal()
    try:
        status = db.query(Status).filter(Status.id == status_id).first()
        if not status:
            return jsonify({'error': 'Status not found'}), 404
        
        status.name = data.get('name', status.name)
        
        db.commit()
        return jsonify({'message': 'Status updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@status_routes.route('/statuses/<int:status_id>', methods=['DELETE'])
def delete_status(status_id):
    db = SessionLocal()
    try:
        status = db.query(Status).filter(Status.id == status_id).first()
        if not status:
            return jsonify({'error': 'Status not found'}), 404
        
        db.delete(status)
        db.commit()
        return jsonify({'message': 'Status deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()
