import requests

# Global Variable
API_URL = "https://api.nasa.gov/neo/rest/v1/feed"

def make_request(query_params):
    response = requests.get(API_URL, params=query_params)
    return response