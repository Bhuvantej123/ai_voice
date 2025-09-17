from flask import Flask
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
client=Groq(api_key="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")

def create_app():
    app=Flask(__name__,instance_relative_config=True)


    app.config.from_pyfile("config.py",silent=True)

    from .routes import main
    app.register_blueprint(main)

    return app