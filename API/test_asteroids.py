from make_requests import make_request
import json

# Run Test with HTML graphic:
# pytest test_asteroids.py --html=./report/report.html
# pytest test_asteroids.py --html-report=./report/report2.html

# Global Variable
API_KEY = "DEMO_KEY"

class TestAsteroids:
    def __int__(self):
        pass

    def test_search_asteroids_with_success(self):
        # Arrange: prepare the context
        query_params = {
            "start_date": "2024-12-09",
            "end_date": "2024-12-16",
            "api_key": API_KEY,
        }
        # Act: prepare the action
        response = make_request(query_params)
        # Assert status code:
        assert response.status_code == 200
        # Assert content-type
        assert response.headers["Content-type"] == "application/json; charset=utf-8"
        # Assertion of body response content
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0
        assert data["element_count"] > 0
        # Displaying data in json format
        response_body_json = json.dumps(data, indent=4)

    def test_search_asteroids_with_query_parameters_empty(self):
        query_params = {}
        response = make_request(query_params)
        assert response.status_code == 403
        data = response.json()
        error_message = {'error': {'code': 'API_KEY_MISSING',
           'message': 'No api_key was supplied. Get one at '
                      'https://api.nasa.gov:443'}}
        assert data == error_message

    def test_search_asteroids_with_start_date(self):
        query_parms = {
            "start_date": "2024-12-09",
            "api_key": API_KEY
        }
        response = make_request(query_parms)
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert data["element_count"] > 0

    def test_search_asteroids_with_end_date(self):
        query_params = {
            "end_date": "2024-12-16",
            "api_key": API_KEY
        }
        response = make_request(query_params)
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert data["element_count"] > 0

    def test_search_asteroids_with_valid_range(self):
        query_params = {
            "start_date": "2024-12-16",
            "end_date": "2024-12-18",
            "api_key": API_KEY
        }
        response = make_request(query_params)
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert data["element_count"] > 0

    def test_search_asteroids_with_invalid_range(self):
        query_params = {
            "start_date": "2024-12-18",
            "end_date": "2024-12-09",
            "api_key": API_KEY
        }
        response = make_request(query_params)
        assert response.status_code == 400
        data = response.json()
        assert len(data) > 0
        assert data["element_count"] > 0

    def test_search_asteroids_with_invalid_token(self):
        query_params = {
            "start_date": "2024-12-09",
            "end_date": "2024-12-10",
            "api_key": "abcdef"
        }
        response = make_request(query_params)
        assert response.status_code == 403
        data = response.json()
        error_message = {'error': {'code': 'API_KEY_INVALID', 'message': 'An invalid api_key was supplied. Get one at https://api.nasa.gov:443'}}
        assert data == error_message
