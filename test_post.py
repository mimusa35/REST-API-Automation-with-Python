#POST Request Test
import requests
from Configure import BASE_URL, HEADERS

def test_post_activity():
    payload = {
        "id": 20,
        "title": "New Activity",
        "description": "This is a new activity",
        "pageCount": 10,
        "excerpt": "New excerpt",
        "publishDate": "2024-12-08T00:00:00.000Z"
    }
    response = requests.post(url = BASE_URL + "/Activities", headers=HEADERS, json=payload)
    assert response.status_code == 200, "POST request failed: {response.status_code}"
    print("POST Response:", response.json())
