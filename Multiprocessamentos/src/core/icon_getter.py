from os import makedirs
from os.path import exists
from shutil import rmtree, copyfileobj
from requests import get
from src.services.poke_api import get_pokemons
from src.services.decorators import calculate_time

PATH = "dowload"


def dowload_file(name, url, *, path=PATH, type_="png"):
    "faz o dowload de um arquivo"

    response = get(url, stream=True, timeout=10)

    file_name = f"{path}/{name}.{type_}"

    with open(file_name, "wb") as f:
        copyfileobj(response.raw, f)
    return file_name


def get_sprite_url(url, sprite="front_default"):
    return get(url, timeout=10).json()["sprites"][sprite]


@calculate_time
def get_icon(limit: int = 10):
    if exists(PATH):
        rmtree(PATH)
    makedirs(PATH)

    pokemons = get_pokemons(limit)
    images_url = {
        pokemon_data["name"]: get_sprite_url(pokemon_data["url"])
        for pokemon_data in pokemons
    }
    files = [dowload_file(name, url) for name, url in images_url.items()]
    print(files)
