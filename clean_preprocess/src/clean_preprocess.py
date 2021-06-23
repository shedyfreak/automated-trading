stepone_rsi = {symbol: None for symbol in available_stocks_list}
stepone_cci = {symbol: None for symbol in available_stocks_list}
stepone_aroon = {symbol: None for symbol in available_stocks_list}
stepone_ema = {symbol: None for symbol in available_stocks_list}
stepone_macd = {symbol: None for symbol in available_stocks_list}
stepone_stoch = {symbol: None for symbol in available_stocks_list}


# This set of functions will take stocks transform them from json to df, store them, and then save them in CSV Format
def preprocess_stocks_prices():
    raw_data = pickle.load(open("../../retrieve_update/src/data/stocks/stock_prices.pickle", "rb"))
    for symbol in raw_data:
        # a part of cleaning is elminating irreleavant elements from data
        (raw_data[symbol]).pop('Meta Data', None)
        x, raw_data[symbol] = raw_data[symbol].popitem()
        for date in raw_data[symbol]:
            for value in raw_data[symbol][date]:
                raw_data[symbol][date][value] = float(raw_data[symbol][date][value])
        raw_data[symbol] = (pd.DataFrame.from_dict(raw_data[symbol])).transpose()
        try:
            clean_helper(raw_data[symbol])
        except CorruptedFields:
            print("""Corrupted Fields detected please relaunch the program 
            or contact the Admin error occured on {} """.format(symbol))
        raw_data[symbol].to_csv("../data_warehouse/stocks/unlabeled_stocks/{}_clean.csv".format(symbol))
        # display(raw_data[symbol])


def preprocess_rsi():
    data = pickle.load(open("../../retrieve_update/src/data/indices/rsi_index.pickle", "rb"))
    for symbol in data:
        (data[symbol]).pop('Meta Data', None)
        x, data[symbol] = data[symbol].popitem()
        for obj in data[symbol]:
            for value in data[symbol][obj]:
                data[symbol][obj][value] = float(data[symbol][obj][value])
        stepone_ema[symbol] = pd.DataFrame.from_dict(data[symbol]).transpose()
        # display(stepone_ema[symbol])


def preprocess_cci():
    data = pickle.load(open("../../retrieve_update/src/data/indices/cci_index.pickle", "rb"))
    for symbol in data:
        (data[symbol]).pop('Meta Data', None)
        x, data[symbol] = data[symbol].popitem()
        for obj in data[symbol]:
            for value in data[symbol][obj]:
                data[symbol][obj][value] = float(data[symbol][obj][value])
        stepone_cci[symbol] = pd.DataFrame.from_dict(data[symbol]).transpose()
        # display(stepone_cci[symbol])


def preprocess_aroon():
    data = pickle.load(open("../../retrieve_update/src/data/indices/aroon_index.pickle", "rb"))
    for symbol in data:
        (data[symbol]).pop('Meta Data', None)
        x, data[symbol] = data[symbol].popitem()
        for obj in data[symbol]:
            for value in data[symbol][obj]:
                data[symbol][obj][value] = float(data[symbol][obj][value])
        stepone_aroon[symbol] = pd.DataFrame.from_dict(data[symbol]).transpose()
        # display(stepone_aroon[symbol])


def preprocess_ema():
    data = pickle.load(open("../../retrieve_update/src/data/indices/ema_index.pickle", "rb"))
    for symbol in data:
        (data[symbol]).pop('Meta Data', None)
        x, data[symbol] = data[symbol].popitem()
        for obj in data[symbol]:
            for value in data[symbol][obj]:
                data[symbol][obj][value] = float(data[symbol][obj][value])
        stepone_ema[symbol] = pd.DataFrame.from_dict(data[symbol]).transpose()
        # display(stepone_ema[symbol])


def preprocess_macd():
    data = pickle.load(open("../../retrieve_update/src/data/indices/macd_index.pickle", "rb"))
    for symbol in data:
        (data[symbol]).pop('Meta Data', None)
        x, data[symbol] = data[symbol].popitem()
        for obj in data[symbol]:
            for value in data[symbol][obj]:
                data[symbol][obj][value] = float(data[symbol][obj][value])
        stepone_macd[symbol] = pd.DataFrame.from_dict(data[symbol]).transpose()
        # display(stepone_macd[symbol])


def preprocess_stoch():
    data = pickle.load(open("../../retrieve_update/src/data/indices/stochastic_index.pickle", "rb"))
    for symbol in data:
        (data[symbol]).pop('Meta Data', None)
        x, data[symbol] = data[symbol].popitem()
        for obj in data[symbol]:
            for value in data[symbol][obj]:
                data[symbol][obj][value] = float(data[symbol][obj][value])
        stepone_stoch[symbol] = pd.DataFrame.from_dict(data[symbol]).transpose()
        # display(stepone_stoch[symbol])


def stepone_preprocess_all():
    preprocess_stocks_prices()
    preprocess_rsi()
    preprocess_cci()
    preprocess_aroon()
    preprocess_ema()
    preprocess_macd()
    preprocess_stoch()
