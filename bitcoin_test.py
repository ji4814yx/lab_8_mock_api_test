import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

""" mock data: bitcoin.get_bitcoin_data and force it to return a value"""


class TestConversion(TestCase):

    @patch('bitcoin.get_bitcoin_data')
    def test_get_bitcoin_data(self, mock_api):
        mock_api.return_value = {
            "time": {"updated": "Oct 12, 2023 00:10:00 UTC", "updatedISO": "2023-10-12T00:10:00+00:00",
                     "updateduk": "Oct 12, 2023 at 01:10 BST"},
            "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
            "chartName": "Bitcoin", "bpi": {
                "USD": {"code": "USD", "symbol": "&#36;", "rate": "26,857.1693", "description": "United States Dollar",
                        "rate_float": 26857.1693}, "GBP": {"code": "GBP", "symbol": "&pound;", "rate": "22,441.6358",
                                                           "description": "British Pound Sterling",
                                                           "rate_float": 22441.6358},
                "EUR": {"code": "EUR", "symbol": "&euro;", "rate": "26,162.8040", "description": "Euro",
                        "rate_float": 26162.804}}}

        expected_float = 26857.1693 * 100
        expected = round(expected_float, 2)
        dollars = bitcoin.convert_bitcoin_to_dollars(100)
        self.assertEqual(expected, dollars)


if __name__ == '__main__':
    unittest.main()
