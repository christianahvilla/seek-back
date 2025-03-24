from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.user import get_user, create_user

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = get_user(email)
    if not user or user['password'] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    additional_claims = {
        "email": user["email"],
        "name": user["name"]
    }
    access_token = create_access_token(identity=email, additional_claims=additional_claims)
    return jsonify(token=access_token), 200


@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    if not email or not name or not password:
        return jsonify({"error": "Email, name, and password are required"}), 400

    try:
        create_user(email, name, password)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Email already exists"}), 400