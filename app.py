import os
from flask import Flask
from flask_migrate import Migrate

from .src.models.base_model import db
from .config import config
from .src.extensions import init_extensions



migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    
    init_extensions(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    print('Migration applied')
    return app

app = create_app(os.getenv("CONFIG_MODE")) 

# ----------------------------------------------- #

# Hello World!
@app.route('/hello')
def hello():
    return "Hello World!"

# ----------------------------------------------- #

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()