from flask import request, abort, jsonify
from passlib.hash import pbkdf2_sha256

from app.services.mongodb_service import MongodbService
from app.services.token_service import TokenService


def register_user():
    print("hello")
    json_input = request.json

    # Check if user already exists
    existing_user = MongodbService.find_one_by_resource(
        resource="users",
        lookup={"username": json_input["username"]}
    )

    if existing_user:
        abort(400, {"message": "Username already exists"})

    # Create new user
    new_user = {
        "username": json_input["username"],
        "password": pbkdf2_sha256.hash(json_input["password"]),
        "role": "user",  # Default role
        "view_access": ['users', 'wiki'],  # Default access
        "edit_access": ['users', 'wiki']  # Default access
    }

    # Insert new user
    result = MongodbService.insert_one_by_resource(
        resource="users",
        data=new_user
    )

    if result.inserted_id:
        return jsonify({"message": "User registered successfully"}), 201
    else:
        abort(500, {"message": "Failed to register user"})


def authenticate_user():
    json_input = request.json
    if not json_input or 'username' not in json_input or 'password' not in json_input:
        abort(400, {"message": "Missing username or password"})

    user = MongodbService.find_one_by_resource(
        resource="users",
        lookup={"username": json_input["username"]}
    )

    if not user:
        abort(401, {"message": "Invalid username or password"})

    if not pbkdf2_sha256.verify(json_input["password"], user["password"]):
        abort(401, {"message": "Invalid username or password"})

    return TokenService.create_user_token(user)
