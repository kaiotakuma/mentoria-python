import requests


# URL da API "The Cat API" para imagens aleatórias de gatos
url = "https://api.thecatapi.com/v1/images/search"

# Fazer uma solicitação GET
response = requests.get(url)


# Verificar o status da resposta
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    data = response.json()
    print(data)

else:
    # Lidar com erros, por exemplo, mostrar uma mensagem de erro
    print(f"Erro na solicitação à API {response.status_code}")
