import requests


def ex_rate_eur():
    url = 'https://currency-exchange.p.rapidapi.com/exchange'

    querystring1 = {'to': 'RUB', 'from': 'EUR', 'q': '1.0'}

    headers = {
        'x-rapidapi-key': '3970ee3114msh4e6f76d84f1e3d8p1ef409jsn6875ada7ef96',
        'x-rapidapi-host': 'currency-exchange.p.rapidapi.com'
    }

    response = requests.request("GET", url, headers=headers, params=querystring1)

    return response.text
