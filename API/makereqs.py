import requests
import json

"""
    Print nicely JSON formatted response from an endpoint get request
    ref: https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/
         https://newsapi.org/
"""

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])

        for index, article in enumerate(articles[:3], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")

def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))

if __name__ == "__main__":
    response = requests.get('https://w3schools.com/python/demopage.htm')
    print(response)

    API_KEY = "GET_API_KEY"
    api_endpoint = f"https://newsapi.org/v2/everything?q=tesla&from=2024-11-02&sortBy=publishedAt&apiKey={API_KEY}"
    fetch_and_print_articles(api_endpoint)

    jprint(response.json())

