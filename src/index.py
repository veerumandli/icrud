from flask import Flask
from .controllers.crud import create_item, fetch_list, fetch_detail
app = Flask(__name__, template_folder='views')


@app.route("/<table_name>", methods=['POST'])
def post_route(table_name):
    return create_item(table_name)


@app.route("/<table_name>", methods=['GET'])
def get_route(table_name):
    return fetch_list(table_name)


@app.route("/<table_name>/<id>", methods=['GET'])
def get_one_route(table_name, id):
    return fetch_detail(table_name, id)
