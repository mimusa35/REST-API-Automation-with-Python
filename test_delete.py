#DELETE Request Test
import requests
from Configure import BASE_URL, HEADERS

def test_delete_activity():
    # Send DELETE request
    response = requests.delete(url = BASE_URL + "/Activities/20", headers=HEADERS)

    # Assert that the status code is 200 or 204 (depending on API behavior)
    assert response.status_code in [200, 204], "DELETE request failed: {response.status_code}"

    # Check if response body is empty
    if response.text.strip():
        print("DELETE Response:", response.json())  # Only parse JSON if the body is not empty
    else:
        print("DELETE Response: No Content")


