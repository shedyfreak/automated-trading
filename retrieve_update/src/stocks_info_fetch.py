#!/usr/bin/env python
# coding: utf-8

# In[7]:


import quandl
import requests
import pickle
import time
import CONSTANTS


def update_snb():
    snb_data = quandl.get("SNB/CAPCHSTOCKI", authtoken="kVxxtbafwx1jrcH7xwps",
                          collapse="weekly", start_date=CONSTANTS.START_DATE, end_date=CONSTANTS.END_DATE)
    file = open(CONSTANTS.SNB_FILENAME, "wb")
    pickle.dump(snb_data, file)


def update_stock_prices():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(CONSTANTS.BASE_URL + "&symbol={}&function=TIME_SERIES_WEEKLY"
                            .format(ticker))
        nb_api_call = nb_api_call + 1
        if "Weekly Time Series" in data.json():
            dataset[ticker] = data.json()

    file = open("data/stocks/raw_stock_data.pickle", "wb")
    pickle.dump(dataset, file)


def update_overview():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(CONSTANTS.BASE_URL + "&symbol={}&function=OVERVIEW"
                            .format(ticker))
        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
    file = open("data/stocks/stock_overview.pickle", "wb")
    pickle.dump(dataset, file)


def update_income_state():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(CONSTANTS.BASE_URL + "&symbol={}&function=INCOME_STATEMENT"
                            .format(ticker))
        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
    file = open("data/stocks/income_statments.pickle", "wb")
    pickle.dump(dataset, file)


def update_balance_sheet():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(CONSTANTS.BASE_URL + "&symbol={}&function=BALANCE_SHEET"
                            .format(ticker))
        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
    file = open("data/stocks/balance_sheet.pickle", "wb")
    pickle.dump(dataset, file)


def update_cash_flow():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(CONSTANTS.BASE_URL + "&symbol={}&function=BALANCE_SHEET"
                            .format(ticker))
        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
    file = open("data/stocks/cash_flow.pickle", "wb")
    pickle.dump(dataset, file)


def update_EMA():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(
            CONSTANTS.BASE_URL + "&interval=weekly&time_period=15&series_type=close&symbol={}&function=EMA"
            .format(ticker))

        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
        file = open("data/indices/ema_index.pickle", "wb")
        pickle.dump(dataset, file)
        file.close()


def update_stoch_index():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(CONSTANTS.BASE_URL + "&interval=weekly&symbol={}&function=stoch"
                            .format(ticker))

        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
        file = open("data/indices/stochastic_index.pickle", "wb")
        pickle.dump(dataset, file)
        file.close()


def update_RSI():
    dataset = {}
    nb_api_call = 0
    for ticker in CONSTANTS.available_stocks_list:
        if nb_api_call == 5:
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(
            CONSTANTS.BASE_URL + "&time_period=10&interval=weekly&series_type=close&symbol={}&function=rsi"
            .format(ticker))

        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
        file = open("data/indices/rsi_index.pickle", "wb")
        pickle.dump(dataset, file)
        file.close()


def update_aroon():
    dataset = {}
    nb_api_call = 0
    for ticker in available_stocks_list:
        if (nb_api_call == 5):
            ### to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(BASE_URL + "&time_period=10&interval=weekly&symbol={}&function=aroon"
                            .format(ticker))

        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
        file = open("retrieve_update/src/data/indices/aroon_index.pickle", "wb")
        pickle.dump(dataset, file)
        file.close()


def update_MACD():
    dataset = {}
    nb_api_call = 0
    for ticker in available_stocks_list:
        if (nb_api_call == 5):
            # to respect maximum 5 API calls per minute
            time.sleep(60)
            nb_api_call = 0
        data = requests.get(BASE_URL + "&interval=weekly&series_type=close&symbol={}&function=macd"
                            .format(ticker))

        nb_api_call = nb_api_call + 1
        dataset[ticker] = data.json()
        print(data.json())
        file = open("retrieve_update/src/data/indices/macd_index.pickle", "wb")
        pickle.dump(dataset, file)
        file.close()


def update_retrieve_all():
    update_aroon()
    update_RSI()
    update_EMA()
    update_snb()
    update_balance_sheet()
    update_cash_flow()
    update_overview()
    update_stoch_index()
    update_stock_prices()
    update_MACD()
