import requests

def get_request(url:str):
    x = requests.get(url)
    print(f"Response: {x}")

url = 'https://w3schools.com'
get_request(url)

    