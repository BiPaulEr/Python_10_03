import copy
prenoms = ["paul", "ernest", "martin"]

def capitalize_liste(liste):
    new_liste = copy.deepcopy(liste)
    for index, valeur in enumerate(new_liste):
        new_liste[index] = valeur.upper()
    return new_liste

print(capitalize_liste)                      

PRENOMS_liste = capitalize_liste(prenoms)

print(prenoms) #['paul', 'ernest', 'martin']
print(PRENOMS_liste) #['PAUL', 'ERNEST', 'MARTIN']

