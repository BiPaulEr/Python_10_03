nom_de_mon_cheval = "Petit Tonnerre"
print("dans le fichier module importe", __name__)

def monter_a_cheval(nom):
    print(f"Je suis sur le cheval {nom}")

if __name__ == "___main__":
    monter_a_cheval("Capucine")