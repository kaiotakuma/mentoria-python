from requests import get


def get_pokemons(limit: str = 1) -> dict:
    base_url = "https://pokeapi.co/api/v2"

    url = f"{base_url}/pokemon/?limit={limit}"
    response = get(url)

    return response.json()["results"]
