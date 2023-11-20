import requests

# Define a URL do endpoint da API
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

# Faz a requisição à API
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (status 200)
if response.status_code == 200:
    data = response.json()
    print(data)

    print("Falha na requisição. Status Code:", response.status_code)
