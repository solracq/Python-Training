import requests
import json
import pytest

# BASE_URL = "https://jsonplaceholder.typicode.com"

# Get the test configuration info from the configuration file
with open("config.json", 'r') as json_file:
    config = json.load(json_file)

class TestRequestsDemo:
    def __int__(self):
        pass

    @pytest.mark.Regression
    def test_get_demo(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        response = requests.get(host+get_api)
        # Assert status code
        # response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
        # Assert content-type
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        # Assert response content/structure
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0
        assert data["userId"] == 1
        assert data["id"] == 1
        data = json.dumps(data, indent=4)

    @pytest.mark.Smoke
    def test_post_demo(self):
        params = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        # Make the request
        host = config.get("host")
        post_api = config.get("postAPI")
        response = requests.post(host+post_api, params=params)
        # response = requests.post(f"{BASE_URL}/posts", params=params)
        # Assert status code
        assert response.status_code == 201
        # Assert content-type
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        # Assert data content structure
        data = response.json()
        assert len(data) > 0
        assert isinstance(data, dict)
        assert data["id"] == 101

    def test_get_book_by_id(self):
        # Make request
        api_url = config.get("mhost")
        api_rqst = config.get("mgetAPI")
        response = requests.get(api_url + api_rqst)
        # Assert status code
        assert response.status_code == 200
        # Assert content-type
        assert response.headers["Content-Type"] == "application/json; charset=UTF-8"
        # Assert response content
        # data = response.json()

    @pytest.mark.parametrize("book_id, status_code", [
        (1, 200),   # Valid book ID
        (999, 404), # Non-existing book ID
    ])
    def test_get_several_books(self):
        # Make request
        api_url = config.get("mhost")
        api_rqst = config.get("mgetAPI")
        response = requests.get(f"{api_url}{api_rqst}/{'book_id'}")
        # Assert status
        assert response.status_code == 200

    def test_create_book_by_id(self):
        # Prameters
        new_book = {
            "title": "A voice in the night",
            "author": "Dean Knootz"
        }
        # Make request
        api_url = config.get("mhost")
        api_prqst = config.get("mpostAPI")
        response = requests.post(api_url + api_prqst, json=new_book)
        # Assert status code
        assert response.status_code == 201
        # Assert content-type
        assert response.headers["Content-Type"] == "application/json; charset=UTF-8"
        # Assert response content, that the book was created
        data = response.json()
        assert data > 0
        assert "id" in data
        assert data["title"] == "A voice in the night"
        assert data["author"] == "Dean Knootz"

    def test_update_book(self):
        params = {
            "title": "Other title"
        }
        # Make request
        api_url = config.get("mhost")
        api_rqst = config.get("mpostAPI")
        book_id = "1"
        response = requests.put(api_url + api_rqst + book_id, params=params)
        # Assert status code
        assert response.status_code == 200
        # Assert content-type
        assert response.headers["Content-Type"] == "application/json; charset=UTF-8"
        # Assert response content
        data = response.json()
        assert len(data) > 0
        assert data["id"] == int(book_id)
        assert data["title"] == params["title"]

    def test_delete_book(self):
        # Make request:
        api_url = config.get("mhost")
        api_rqst = config.get("mpostAPI")
        book_id = "1"
        response = requests.delete(api_url + api_rqst + book_id)
        # Assert status code
        assert response.status_code == 204   # Successful deletion
        # Assert response content
        data = response.txt
        assert data == ""   # Verify empty response body
