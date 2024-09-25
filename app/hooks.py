from bson import ObjectId
from flask import abort
from app.services.token_service import TokenService
from app.services.mongodb_service import MongodbService

def authorize_and_control_access(resource, access_type, request):
    decoded_token = authorize_token(request)
    return control_access(resource, access_type, decoded_token)

def pre_get_all(resource, request, lookup):
    authorize_and_control_access(resource, 'view_access', request)

def pre_post_all(resource, request):
    authorize_and_control_access(resource, 'edit_access', request)

def pre_put_all(resource, request, lookup):
    authorize_and_control_access(resource, 'edit_access', request)

def pre_patch_all(resource, request, lookup):
    authorize_and_control_access(resource, 'edit_access', request)

def pre_delete_all(resource, request, lookup):
    authorize_and_control_access(resource, 'edit_access', request)

def authorize_token(request):
    token = request.headers.get('token')
    if not token:
        abort(401, {"error": "Missing token"})
    return TokenService.decode_token(token)

def control_access(resource, access_type, decoded_token):
    user = MongodbService.find_one_by_resource(
        resource='users', 
        lookup={"_id": ObjectId(decoded_token['u_id'])}
    )

    if resource not in user[access_type]:
        abort(403, {"message": "Access Forbidden"})
    return user