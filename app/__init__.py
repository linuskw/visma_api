from eve import Eve
from flask_cors import CORS

from app.hooks import pre_get_all, pre_post_all, pre_put_all, pre_patch_all, pre_delete_all
from app.services.mongodb_service import MongodbService
from app.auth import register_user, authenticate_user
from app.resources import DOMAIN as resources_domain


def create_app():
    app = Eve()
    CORS(app)

    MongodbService.global_init(app=app)

    app.route('/register', methods=['POST'])(register_user)
    app.route('/authenticate', methods=['POST'])(authenticate_user)

    # Hooks
    app.on_pre_GET += pre_get_all
    app.on_pre_POST += pre_post_all
    app.on_pre_PUT += pre_put_all
    app.on_pre_PATCH += pre_patch_all
    app.on_pre_DELETE += pre_delete_all

    return app
