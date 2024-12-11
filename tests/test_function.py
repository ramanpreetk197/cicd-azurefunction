import requests

def test_hello_world():
    url = "http://<your-function-url>"  # Replace with your actual function URL
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.text == "Hello, World!"
