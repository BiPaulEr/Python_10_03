#exerice 1
nombres = [1, -1, 2, -2, 3, -3]

for nombre in nombres:
    if nombre < 0:
        continue
    print(nombre)

#exercice 2
mots_de_passes = ["12345678", "password123", "abc123", "pythoniscool"]
for mdp in mots_de_passes:
    if len(mdp) < 8:
        print("Mot de passe faible")
        break

#exerice 3
elements = ['pomme', 'banane', 'cerise', 'date', 'banane', 'baie']
element_deja_eu = []
for element in elements:
    if element in element_deja_eu:
        print("Element double trouve ", element)
        break
    print(element)
    element_deja_eu.append(element)

