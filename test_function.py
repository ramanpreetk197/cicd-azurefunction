import pytest
from unittest.mock import Mock
import app

def test_hello_world():
    req = Mock()  # Mock the HttpRequest
    response = app.main(req)
    
    assert response.status_code == 200
    assert response.get_body() == b"Hello, World!"
