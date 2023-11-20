import requests
import json

URL_POSITION = 'https://k8s.gorila.com.br/position/api/v1'

def get_position_gorila(fund_id: str, max_date: str):


    params = {
        "datePeriod": "DAILY",
        "maxDate": max_date,
        "includeNoPrice": "true",
        "forceCurrent": "true",
    }

    response = requests.get(
        f"{URL_POSITION}/portfolios/{fund_id}/positions", params=params
    )
    return response.json()

print(json.dumps(get_position_gorila("1666849","2023-10-27")))