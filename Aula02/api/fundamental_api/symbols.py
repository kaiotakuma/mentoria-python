import requests


url_fundamental = "https://fundamental-app.fly.dev"


def get_indicators(symbol: str, date: str):


    url = f"{url_fundamental}/symbols/{symbol}"
    print(url)

    response = requests.get(url, json={"date": date})


    return response.json()


print(get_indicators("VALE3", "2023-10-27"))



# /symbols/VALE3


# def get_position_btg(account_number, date):
#     access_token = get_access_token()

#     manage_rate_limit(access_token)

#     request_id = generate_partner_request()
#     headers = {
#         "x-id-partner-request": f"{request_id}",
#         "access_token": f"{access_token}",
#     }

#     url = f"{os.getenv('BTG_URL')}/iaas-api-position/api/v1/position/{account_number}"
#     response = requests.post(url, headers=headers, json={"date": date})

#     return response.json()
