"""This tests the CSV functions"""
import os

import flask_login
from flask import session

from app import db
from app.db.models import User, Song


def test_upload_song_csv(test_client, add_user):
    #user = add_user
    #flask_login.login_user(user)

    with test_client.session_transaction() as session:
        response = test_client.post('/login', data=dict(email="keith@webizly.com", password="testtest"))
        print("\n"+ str(session.get('csrf_token')))
        assert response.status_code == 200

    #songs = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "music.csv"))
    #csv_data = open(songs, "rb")
    #data = {"file": (csv_data, "music.csv")}
    #response = test_client.post('/songs/upload', data=data)
    #assert response.status_code == 200