from flask import request, jsonify
from . import department_routes
from models.department import Department

@department_routes.route('/departments', methods=['POST'])
def create_department():
    data = request.get_json()
    new_department = Department(name=data['name'])
    # Add logic to save the department to the database
    return jsonify({'message': 'Department created successfully'}), 201

@department_routes.route('/departments', methods=['GET'])
def get_departments():
    # Add logic to retrieve all departments from the database
    return jsonify(departments), 200
