"""The tests the logging"""

import os


def test_log_files_exists():
    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app/logs/errors.log"))) == True
    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app/logs/flask.log"))) == True
    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app/logs/myapp.log"))) == True
    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app/logs/request.log"))) == True
    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app/logs/sqlalchemy.log"))) == True
    assert os.path.exists(
        os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app/logs/werkzeug.log"))) == True
