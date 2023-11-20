import requests
from PIL import Image

# URL da API "The Cat API" para imagens aleatórias de gatos
url = "https://api.thecatapi.com/v1/images/search"

# Fazer uma solicitação GET
response = requests.get(url)
print(response)

# Verificar o status da resposta
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    data = response.json()
    image_url = data[0]["url"]
else:
    # Lidar com erros, por exemplo, mostrar uma mensagem de erro
    print(f"Erro na solicitação à API {response.status_code}")

# Exibir a imagem
image = Image.open(requests.get(image_url, stream=True).raw)
image.show()
