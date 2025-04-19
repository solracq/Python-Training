import requests
import json

"""
CURRENCY_EXCHANGE_RATE API function returns the realtime exchange rate
of any pair of digital or physical currency.
For more info: https://www.alphavantage.co/documentation/
"""

# API endpoint and key
API_URL = "https://www.alphavantage.co/query"
API_KEY = "GET_API_KEY"

def get_currency_exchange():
    # Parameters for the API:
    params={
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "CAD",
        "to_currency": "MXN",
        "apikey": API_KEY,
    }

    # Making API request
    response = requests.get(API_URL, params=params)

    # Checking if the response is successfull
    if response.status_code == 200:
        # Getting the JSON response
        # data = response.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
        data = response.json()
        return data
    else:
        return None

def print_result(data: dict):
    for key, value in data.items():
        print(f"{key}")
        for k, v in value.items():
            print(k, v)

if __name__ == "__main__":
    print_result(get_currency_exchange())
    # print(get_currency_exchange())