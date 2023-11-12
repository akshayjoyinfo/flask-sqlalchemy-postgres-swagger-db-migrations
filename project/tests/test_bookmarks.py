
import pytest
import json


from project.app import create_app
from project.app import db


def test_bookmakrs(app, client):
    res = client.get('/api/v1/bookmarks')
    data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    assert data["meta"]["total_count"] == 26

def test_bookmakrs_extra(app, client):
    res = client.get('/api/v1/bookmarks')
    data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    assert data["meta"]["total_count"] == 26