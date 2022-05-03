"""This tests the CSV functions"""
import os

def test_upload_song_csv(test_client):
    response = test_client.post('/login', data=dict(email="keith@webizly.com", password="testtest"),
                                follow_redirects=True)
    assert response.status_code == 200

    songs = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "music.csv"))
    csv_data = open(songs, "rb")
    data = {"file": (csv_data, "music.csv")}
    response = test_client.post('/songs/upload', data=data, follow_redirects=True, buffered=True,
                                content_type='multipart/form-data')
    assert response.status_code == 200
    response = test_client.get("/songs")
    assert response.status_code == 200


def test_upload_location_csv(test_client):
    response = test_client.post('/login', data=dict(email="keith@webizly.com", password="testtest"),
                                follow_redirects=True)
    assert response.status_code == 200

    songs = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "us_cities_short.csv"))
    csv_data = open(songs, "rb")
    data = {"file": (csv_data, "us_cities_short.csv")}
    response = test_client.post('/locations/upload', data=data, follow_redirects=True, buffered=True,
                                content_type='multipart/form-data')
    assert response.status_code == 200
    response = test_client.get("/locations/map")
    assert response.status_code == 200
