from flask import Flask

def create_app():
    app = Flask(__name__)

    # import routes inside factory to avoid circular imports
    from .routes import main
    app.register_blueprint(main)

    return app
