from datetime import datetime
from os import makedirs
from os.path import exists
from shutil import rmtree , copyfileobj
from urllib.parse import urljoin
from requests import get 

## Sem paralelismo 0:01:12.401641

PATH = 'dowload'
base_url = 'https://pokeapi.co/api/v2/'

def dowload_file(name, url , * , path= PATH , type_='png'):
    "faz o dowload de um arquivo"

    response  = get(url,stream=True)

    file_name = f'{path}/{name}.{type_}'

    with open(file_name, 'wb') as f:
        copyfileobj(response.raw, f)
    return file_name

def get_sprite_url(url, sprite = 'front_default'):
    return get(url).json()['sprites'][sprite]

start_time = datetime.now()

if exists(PATH): # Se a pasta exisitr eu removo ela e crio novamente 
    rmtree(PATH)
makedirs(PATH)


pokemons = get(urljoin(base_url,'pokemon/?limit=100')).json()['results']



images_url = {pokemon_data['name']:get_sprite_url(pokemon_data['url']) for pokemon_data in pokemons}


print(images_url)

files = [dowload_file(name, url) for name , url in images_url.items()]

print(files)
time_elapsed = datetime.now() - start_time

print(time_elapsed)
