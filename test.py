#!/usr/bin/python3
# Python program to get the real-time
# currency exchange rate
import random,json
import requests
import urllib.request as urllib2

# Function to get real time currency exchange
# def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key):
#     # importing required libraries
#     import requests, json
#
#     # base_url variable store base url
#     base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
#
#     # main_url variable store complete url
#     main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
#     print(main_url)
#
#
#     # get method of requests module
#     # return response object
#     req_ob = requests.get(main_url)
#
#     # json method return json format
#     # data into python dictionary data type.
#
#     # result contains list of nested dictionaries
#     result = req_ob.json()
#
#     print(" Result before parsing the json data :\n", result)
#
#     # print("\n After parsing : \n Realtime Currency Exchange Rate for",
#     #       result["Realtime Currency Exchange Rate"]
#     #       ["2. From_Currency Name"], "TO",
#     #       result["Realtime Currency Exchange Rate"]
#     #       ["4. To_Currency Name"], "is",
#     #       result["Realtime Currency Exchange Rate"]
#     #       ['5. Exchange Rate'], to_currency)

# Driver code
if __name__ == "__main__":
    # currency code
    from_currency = "USD"
    to_currency = "EGP"

    # enter your api key here
    api_key = "HY18FM7WZPM7CS78"

    # function calling
    # RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key)

    print(json_rpc("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EGP&apikey=HY18FM7WZPM7CS78"))