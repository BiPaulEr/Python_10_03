prenoms = ["paul", "ernest", "martin"]

for index, prenom in enumerate(prenoms):
    prenoms[index] = prenom.capitalize()

noms = ["dupont", "lefevre", "agouyi"] 

for index, nom in enumerate(noms):
    noms[index] = nom.capitalize()

nations = ["fr", "gb", "sc"] 

for index, nation in enumerate(nations):
    nations[index] = nation.capitalize()

print(prenoms, noms, nations)