from flask import Flask

from PomoApp.blueprints.page import page

def create_app():
    """
    Create Flask application using the app factory pattern

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True, static_folder='static')

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)
    
    # @app.route('/')
    # def index():
    #     """
    #     Render a Hello World response to test the local run.

    #     :return: Flask response
    #     """
    #     return app.config['HELLO']

    return app
