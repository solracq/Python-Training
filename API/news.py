import requests
import json

"""
API to search for the worldwide news with code
ref: https://newsapi.org/docs/endpoints/everything
"""

# API endpoint and key
API_URL = f"https://newsapi.org/v2/top-headlines"
API_KEY = "GET_API_KEY"

def get_news():
    # Parameters for the API
    params = {
        "q": "bbc",
        "from": "2024-11-02",
        "sortBy": "publishedAt",
        "domains": "bbc.co.uk",
        # "language": "es",
        "apikey": API_KEY,
    }

    # Making the API request
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for index, article in enumerate(articles[:3], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    get_news()