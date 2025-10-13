from flask import Blueprint
from src.controllers.CrudController import CrudController
from src.core.Decorators import model_from_path


crud_route = Blueprint('crud', __name__, url_prefix='/api/v1')


# -------------------------
# READ ALL (GET)
# -------------------------


@crud_route.route("/<table_name>", methods=['GET'])
@model_from_path
def get_route(Model):
    return CrudController.fetch_list(Model)

# -------------------------
# READ ONE (GET by ID)
# -------------------------


@crud_route.route("/<table_name>/<id>", methods=['GET'])
@model_from_path
def get_one_route(Model, id):
    return CrudController.fetch_detail(Model, id)

# -------------------------
# CREATE (POST)
# -------------------------


@crud_route.route("/<table_name>", methods=['POST'])
@model_from_path
def post_route(Model):
    return CrudController.create_item(Model)


# -------------------------
# UPDATE (POST)
# -------------------------


@crud_route.route("/<table_name>/<id>", methods=['PUT'])
@model_from_path
def put_route(Model, id):
    return CrudController.update_item(Model, id)


# -------------------------
# DELETE (POST)
# -------------------------
@crud_route.route("/<table_name>/<id>", methods=['DELETE'])
@model_from_path
def delete_route(Model, id):
    return CrudController.delete_item(Model, id)
