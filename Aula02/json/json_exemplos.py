import json


exemplo_dict = {
    "nome": "pini",
    "idade": 96,
    "especie": "vampiro",
    "temperatura_corporal": -30.1,
}





with open("exemplo_json_saida.json", 'w',encoding="utf8") as arquivo:
    json.dump(exemplo_dict, arquivo)



# print(exemplo_json)
# print(type(exemplo_json))