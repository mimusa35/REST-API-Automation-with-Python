#GET Request Test
import requests
from Configure import BASE_URL, HEADERS

def test_get_activity():
    response = requests.get(url = BASE_URL + "/Activities/12", headers=HEADERS)
    assert response.status_code == 200, "GET request failed: {response.status_code}"
    print("GET Response:", response.json())
