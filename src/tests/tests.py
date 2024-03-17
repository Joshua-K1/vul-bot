import requests

def test_vul_check():
    url = "http://127.0.0.1:8000/vulnerability-check?query=test"
    response = requests.get(url)
    assert response.status_code == 200

def test_info_check():
    url = "http://127.0.0.1:8000/info-check?query=test"
    response = requests.get(url)
    assert response.status_code == 200
