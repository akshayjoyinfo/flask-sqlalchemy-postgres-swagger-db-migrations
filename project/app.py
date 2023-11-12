import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from flask import Flask
from flask_migrate import Migrate

from project.models.base_model import db
from project.extensions import init_extensions

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class AppConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class PytestConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("PYTEST_DATABASE_URL")

config_section = {
    "main": AppConfig,
    "pytest": PytestConfig
}



migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    if os.environ.get("CONFIG_MODE") == "pytest":
        app.config.from_object(PytestConfig)
        print('inside main applied')
    else:
        app.config.from_object(AppConfig)
        
    init_extensions(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    return app



if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    app = create_app("main") 
    app.run()