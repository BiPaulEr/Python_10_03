import psg

print(psg.liverpool)

import requests
import ast
headers = {"Accept" : "application/json"}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)
if response.status_code == 200:
    print("Requête réussie !")
    print("Contenu de la réponse :", response.text)
    dict = ast.literal_eval(response.text)
    print("joke :", dict.get("joke", "not foudn"))
else:
    print("La requête a échoué avec le code :", response.status_code)