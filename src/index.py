from flask import Flask, render_template
from src.routes.crud import crud_route
from src.routes.home import home_route


def create_app():
    app = Flask(__name__, template_folder='views')
    app.register_blueprint(home_route)
    app.register_blueprint(crud_route)
    return app
