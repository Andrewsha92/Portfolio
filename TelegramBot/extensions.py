import requests
from config import keys
import json

class ConvertionExсeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExсeption(f"Невозможно перевести одинаковые валюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExсeption(f"Не удалось обработать валюту {quote}.")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExсeption(f"Не удалось обработать валюту {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExсeption(f"Не удалось обработать количество {amount}.")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base


