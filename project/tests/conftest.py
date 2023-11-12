from project.app import create_app
from project.app import db
import pytest
from flask_migrate import upgrade,downgrade

@pytest.fixture
def app():
    test_app = create_app()
    print(test_app.config["SQLALCHEMY_DATABASE_URI"])
    with test_app.app_context():
        upgrade()
    yield test_app
@pytest.fixture
def client(app):
    return app.test_client()