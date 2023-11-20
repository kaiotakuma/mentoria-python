import requests


# URL da API do The Dog API para imagens aleatórias
url = "https://api.thedogapi.com/v1/images/search"

# Fazer uma solicitação GET
response = requests.get(url)

# Verificar o status da resposta
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    data = response.json()
    print(data)

else:
    # Lidar com erros, por exemplo, mostrar uma mensagem de erro
    print("Erro na solicitação à API")
