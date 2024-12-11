import app

def test_hello_world():
    req = None  # Mock request object
    response = app.main(req)
    assert response.status_code == 200
    assert response.get_body() == b"Hello, World!"
