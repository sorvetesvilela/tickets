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
        if not all(key in data for key in ('username', 'password', 'email')):
            return jsonify({'error': 'Missing fields in request'}), 400
        
        # Check for existing user
        existing_user = db.query(User).filter((User.username == data['username']) | (User.email == data['email'])).first()
        if existing_user:
            return jsonify({'error': 'Username or email already exists'}), 400
        
        new_user = User(username=data['username'], password=data['password'], email=data['email'])
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()
