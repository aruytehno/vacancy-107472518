import requests


class CurrencyService:
    API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'

    @staticmethod
    def get_exchange_rate():
        response = requests.get(CurrencyService.API_URL)
        if response.status_code == 200:
            data = response.json()
            return data.get('rates', {}).get('RUB')
        return None
