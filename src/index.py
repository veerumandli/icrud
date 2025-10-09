from flask import Flask
from src.controllers.crud import create_item, fetch_detail,fetch_list

from src.core.Decorators import model_from_path



app = Flask(__name__, template_folder='views')


@app.route("/", methods=['GET'])
def home():
    return "<h1>Welcome to iCRUD</h1>"

# -------------------------
# CREATE (POST)
# -------------------------


@app.route("/api/<table_name>", methods=['POST'])
@model_from_path
def post_route(Model):
    return create_item(Model)

# -------------------------
# READ ALL (GET)
# -------------------------

@app.route("/api/<table_name>/all", methods=['GET'])
@model_from_path
def get_route(Model):
    return fetch_list(Model)

# -------------------------
# READ ONE (GET by ID)
# -------------------------


@app.route("/api/<table_name>/<int:id>", methods=['GET'])
@model_from_path
def get_one_route(Model, id):
    return fetch_detail(Model, id)


# -------------------------
# APP RUNNER
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
    
