import pickle
from datetime import date
import sys
import os
sys.path.append(os.getcwd()+'/CONSTANTS.py')
BASE_URL = """https://www.alphavantage.co/query
                      ?apikey=YCVISHALBF20DTQP"""
START_DATE = "2005-01-01"
END_DATE = date.today()
SNB_FILENAME = "data/indices/snb_data.pickle"
available_stocks_list = pickle.load(open("data/stocks/traded_stocks.pickle", "rb"))
