import requests
import json

"""
Program to request for questions from StackOverflow via API requests.
https://api.stackexchange.com/docs/questions
"""
API_URL = "http://api.stackexchange.com/2.3/questions?"

def get_specific_stackoverflow_questions():
    params = {
        "order": "desc",
        "sort": "activity",
        "site": "stackoverflow",
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        for item in response.json()['items']:
            print(f"* Title: {item['title']} \n  Is answered: {item['is_answered']} \n  Link: {item['link']}")

if __name__ == "__main__":
    get_specific_stackoverflow_questions()