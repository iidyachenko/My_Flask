from flask import Flask, request

from blog.articles.views import articles
from blog.main.views import index
from blog.user.views import users


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(index)
    app.register_blueprint(articles)
