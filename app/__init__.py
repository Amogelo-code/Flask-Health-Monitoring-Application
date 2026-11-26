from app.routes import index
from flask import Flask

def create_app():
    app = Flask(__name__)
    index(app)
    return app


