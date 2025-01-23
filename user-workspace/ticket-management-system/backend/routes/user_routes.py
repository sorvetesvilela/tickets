from flask import request, jsonify
from . import user_routes
from models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from database import SessionLocal

@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    db = SessionLocal()
    try:
        if not all(key in data for key in ('username', 'password', 'email')):
            return jsonify({'error': 'Missing fields in request'}), 400
        
        new_user = User(username=data['username'], password=data['password'], email=data['email'])
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == data['username'], User.password == data['password']).first()
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    db = SessionLocal()
    try:
        current_user_id = get_jwt_identity()
        if current_user_id != user_id:
            return jsonify({'error': 'Unauthorized to update this user'}), 403
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        # Password update logic can be added here
        
        db.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    db = SessionLocal()
    try:
        current_user_id = get_jwt_identity()
        if current_user_id != user_id:
            return jsonify({'error': 'Unauthorized to delete this user'}), 403
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        db.delete(user)
        db.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    finally:
        db.close()
