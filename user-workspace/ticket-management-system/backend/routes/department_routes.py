from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models.department import Department
from database import SessionLocal

department_routes = Blueprint('department_routes', __name__)

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

@department_routes.route('/departments', methods=['POST'])
def create_department():
    data = request.get_json()
    schema = DepartmentSchema()
    try:
        validated_data = schema.load(data)
        db = SessionLocal()
        new_department = Department(name=validated_data['name'])
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        return schema.dump(new_department), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        db.close()
