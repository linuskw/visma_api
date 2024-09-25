import os
from app.resources import DOMAIN as RESOURCES_DOMAIN

MONGO_URI = "mongodb://127.0.0.1:27017/visma_work_test"
MONGO_DB = "visma_work_test"

SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
TOKEN_EXPIRATION_MINUTES = int(
    os.environ.get('TOKEN_EXPIRATION_MINUTES', 60))

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = RESOURCES_DOMAIN
