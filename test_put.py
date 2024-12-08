#PUT Request Test
import requests
from Configure import BASE_URL, HEADERS

def test_put_activity():
    payload = {
        "id": 12,
        "title": "Updated Activity",
        "description": "This activity was updated",
        "pageCount": 5,
        "excerpt": "Updated excerpt",
        "publishDate": "2024-12-08T00:00:00.000Z"
    }
    response = requests.put(url = BASE_URL + "/Activities/12", headers=HEADERS, json=payload)
    assert response.status_code == 200, "PUT request failed: {response.status_code}"
    print("PUT Response:", response.json())

