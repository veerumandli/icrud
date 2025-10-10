from flask import Flask, render_template
from src.controllers.crud import create_item, fetch_detail, fetch_list, update_item, delete_item

from src.core.Decorators import model_from_path


app = Flask(__name__, template_folder='views')


@app.route("/", methods=['GET'])
def home():
    return render_template("home/index.html")

# -------------------------
# READ ALL (GET)
# -------------------------


@app.route("/api/<table_name>", methods=['GET'])
@model_from_path
def get_route(Model):
    return fetch_list(Model)

# -------------------------
# READ ONE (GET by ID)
# -------------------------


@app.route("/api/<table_name>/<id>", methods=['GET'])
@model_from_path
def get_one_route(Model, id):
    return fetch_detail(Model, id)

# -------------------------
# CREATE (POST)
# -------------------------


@app.route("/api/<table_name>", methods=['POST'])
@model_from_path
def post_route(Model):
    return create_item(Model)


# -------------------------
# UPDATE (POST)
# -------------------------


@app.route("/api/<table_name>/<id>", methods=['PUT'])
@model_from_path
def put_route(Model, id):
    return update_item(Model, id)


# -------------------------
# DELETE (POST)
# -------------------------
@app.route("/api/<table_name>/<id>", methods=['DELETE'])
@model_from_path
def delete_route(Model, id):
    return delete_item(Model, id)


# -------------------------
# APP RUNNER
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
