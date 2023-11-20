import requests
from PIL import Image
# URL da API do The Dog API para imagens aleatórias
url = "https://api.thedogapi.com/v1/images/search"

# Fazer uma solicitação GET
response = requests.get(url)
print(response.json())

# Verificar o status da resposta
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    data = response.json()
    image_url = data[0]["url"]
else:
    # Lidar com erros, por exemplo, mostrar uma mensagem de erro
    print("Erro na solicitação à API")

# Exibir a imagem
image = Image.open(requests.get(image_url, stream=True).raw)
image.show()