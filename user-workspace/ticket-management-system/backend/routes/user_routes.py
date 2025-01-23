from flask import request, jsonify
from . import user_routes
from models.user import User
from flask_jwt_extended import create_access_token
from database import SessionLocal

@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    db = SessionLocal()
    try:
        new_user = User(username=data['username'], password=data['password'], email=data['email'])
        
        # Save the user to the database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        db.close()

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Add logic to verify user credentials
    access_token = create_access_token(identity=data['username'])
    return jsonify(access_token=access_token), 200
