from flask import Flask
from .controllers.crud import create_item, fetch_list, fetch_detail
from src.core.Decorators import model_from_path

app = Flask(__name__, template_folder='views')


@app.route("/<table_name>", methods=['POST'])
@model_from_path
def post_route(Model):
    return create_item(Model)


@app.route("/<table_name>", methods=['GET'])
@model_from_path
def get_route(Model):
    return fetch_list(Model)


@app.route("/<table_name>/<id>", methods=['GET'])
@model_from_path
def get_one_route(Model, id):
    return fetch_detail(Model, id)
