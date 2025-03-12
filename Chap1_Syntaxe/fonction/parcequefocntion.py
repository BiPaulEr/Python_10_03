prenoms = ["paul", "ernest", "martin"]
noms = ["dupont", "lefevre", "agouyi"] 
nations = ["fr", "gb", "sc"] 

def capitalize_liste(liste):
    for index, valeur in enumerate(liste):
        liste[index] = valeur.upper()

print(capitalize_liste)                      

capitalize_liste(prenoms)

print(prenoms, noms, nations)