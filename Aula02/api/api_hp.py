import requests
from PIL import Image
from io import BytesIO

# URL da API
url = "https://hp-api.onrender.com/api/characters"

# Faz uma solicitação GET à API
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta JSON em um objeto Python
    data = response.json()
    
    # Nome do personagem que você deseja buscar
    # Severus Snape, Minerva McGonagall, Remus Lupin, Sirius Black, Draco Malfoy, Hermione Granger
    personagem_desejado = "Severus Snape"

    # Procura o personagem pelo nome na lista de personagens
    for personagem in data:
        if personagem["name"] == personagem_desejado:
            # Exibe as informações do personagem
            print("Nome:", personagem["name"])
            print("Espécie:", personagem["species"])
            print("Gênero:", personagem["gender"])
            print("Casa:", personagem["house"])
            print("Data de Nascimento:", personagem["dateOfBirth"])
            print("Varinha:", personagem["wand"]["wood"], personagem["wand"]["core"], personagem["wand"]["length"])
            print("Patronus:", personagem["patronus"])
            print("Hogwarts Student:", personagem["hogwartsStudent"])
            print("Hogwarts Staff:", personagem["hogwartsStaff"])
            print("Ator:", personagem["actor"])

            # Exibe a imagem do personagem
            image_url = personagem["image"]
            response_image = requests.get(image_url)
            img = Image.open(BytesIO(response_image.content))
            img.show()
            break
    else:
        print("Personagem não encontrado.")
else:
    print("Erro na solicitação à API. Código de status:", response.status_code)
