from flask import render_template


class HomeController:

    def welcome():
        return render_template("home/index.html")
