import requests
import json

"""
Extract stock price by the help of API. Alpha Vantage API
Ref: https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/
"""


# Function to get live stock data for a symbol
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
def get_stock_data():
    # API endpoint and key
    API_URL = "https://www.alphavantage.co/query"
    API_KEY = "GET_API_KEY"

    # Parameters for the API
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": "IBM",
        "interval": "5min",
        "outputsize": "full",
        # "country": "us",
        # "datatype": "csv",
        "apikey": API_KEY,
    }
    # Making the API request
    response = requests.get(API_URL, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        # Getting the JSON response
        data_res = response.json()
        last_refreshed = data_res['Meta Data']['3. Last Refreshed']
        price = data_res['Time Series (5min)'][last_refreshed]['1. open']
        return price
    else:
        return None


stock_prices = {}
price = get_stock_data()
symbol="IBM"
if price is not None:
    stock_prices[symbol] = price
print(f"{stock_prices}")

