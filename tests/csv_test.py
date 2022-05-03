"""This tests the CSV functions"""
import os

def test_upload_song_csv(test_client, application):
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    response = test_client.post('/login', data=dict(email="test@test.com", password="testtest"),
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

    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads', 'music.csv'))) == True


def test_upload_location_csv(test_client, application):
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    response = test_client.post('/login', data=dict(email="test@test.com", password="testtest"),
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

    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads', 'us_cities_short.csv'))) == True
