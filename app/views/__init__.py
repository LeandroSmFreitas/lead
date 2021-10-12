from flask import Flask, Blueprint

bp = Blueprint("lead", __name__)

def init_app(app:Flask):
    app.register_blueprint(bp)