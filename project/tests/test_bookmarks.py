
import pytest
import json

from flask import jsonify

from project.app import create_app
from project.app import db


def test_bookmakrs(app, client):
    res = client.get('/api/v1/bookmarks')
    data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    # assert data["meta"]["total_count"] == 7

def test_bookmakrs_extra(app, client):
    res = client.get('/api/v1/bookmarks')
    data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    # assert data["meta"]["total_count"] == 7

def test_bookmarks_add(app,client):
    data=json.dumps({
        'body': "Testing Flask",
        'url': "http://some-test.com",
    })
    response = client.post("/api/v1/bookmarks", data=data,headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 201

#def test_bookmarks_put(app,client):
#    data=json.dumps({
#        'body': "Testing Flask 123",
#    })
#    response = client.put("/api/v1/bookmarks/4", data=data,headers={"Content-Type": "application/json"},
#    )
#
#    assert response.status_code == 200
#
# def test_bookmarks_delete(app,client):
#    response = client.delete("/api/v1/bookmarks/17",headers={"Content-Type": "application/json"},
#    )
#
#    assert response.status_code == 200