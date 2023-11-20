import requests


USER_API = "https://k8s-dev.gorila.com.br/user-api/v1"


def sing_up(username: str, password: str, name: str, type: str):
    json = {
        "username": username,
        "password": password,
        "name": name,
        "type": type,
    }
    response = requests.post(f"{USER_API}/signup", json=json)
    return response.status_code


print(sing_up("lennon3_hp@gorilainvest.com.br", "123456", "lennon2", "ADVISOR"))


