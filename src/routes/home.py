from flask import Blueprint
from src.controllers.HomeController import HomeController
home_route = Blueprint('home', __name__)


@home_route.route("/", methods=['GET'])
def home():
    return HomeController.welcome()
