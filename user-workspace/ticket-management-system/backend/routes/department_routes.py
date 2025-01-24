from flask import request, jsonify
from . import department_routes
from models.department import Department
from marshmallow import Schema, fields, ValidationError

class DepartmentSchema(Schema):
    name = fields.Str(required=True)
from database import SessionLocal

@department_routes.route('/departments', methods=['POST'])
def create_department():
    data = request.get_json()
    db = SessionLocal()
    try:
        new_department = Department(name=data['name'])
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        return jsonify({'message': 'Department created successfully', 'department_id': new_department.id}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@department_routes.route('/departments', methods=['GET'])
def get_departments():
    db = SessionLocal()
    try:
        departments = db.query(Department).all()
        return jsonify([{'id': department.id, 'name': department.name} for department in departments]), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@department_routes.route('/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    data = request.get_json()
    db = SessionLocal()
    try:
        department = db.query(Department).filter(Department.id == department_id).first()
        if not department:
            return jsonify({'error': 'Department not found'}), 404
        
        department.name = data.get('name', department.name)
        
        db.commit()
        return jsonify({'message': 'Department updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@department_routes.route('/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    db = SessionLocal()
    try:
        department = db.query(Department).filter(Department.id == department_id).first()
        if not department:
            return jsonify({'error': 'Department not found'}), 404
        
        db.delete(department)
        db.commit()
        return jsonify({'message': 'Department deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()
