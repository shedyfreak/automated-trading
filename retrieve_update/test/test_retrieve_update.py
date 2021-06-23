import unittest
import pickle


class MyTestCase(unittest.TestCase):
    def test_type_update_stocks_prices(self):
        file = open("../src/data/stocks/stock_prices.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(type(data) == dict)
        file.close()

    def test_full_update_stocks_prices(self):
        file = open("../src/data/stocks/stock_prices.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(data != {})
        file.close()

    def test_type_update_overview(self):
        file = open("../src/data/stocks/stock_overview.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(type(data) == dict)
        file.close()

    def test_full_update_overview(self):
        file = open("../src/data/stocks/stock_overview.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(data != {})
        file.close()

    def test_type_update_cashflow(self):
        file = open("../src/data/stocks/cash_flow.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(type(data) == dict)
        file.close()

    def test_full_update_cashflow(self):
        file = open("../src/data/stocks/cash_flow.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(data != {})
        file.close()

    def test_type_update_balancesheet(self):
        file = open("../src/data/stocks/balance_sheet.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(type(data) == dict)
        file.close()

    def test_full_update_balancesheet(self):
        file = open("../src/data/stocks/balance_sheet.pickle", "rb")
        data = pickle.load(file)
        self.assertTrue(data != {})
        file.close()


if __name__ == '__main__':
    unittest.main()
