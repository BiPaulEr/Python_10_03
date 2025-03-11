prenoms = ["paul", "ernest", "martin"]

print(list(enumerate(prenoms)))
#[(0, 'paul'), (1, 'ernest'), (2, 'martin')]

for valeur in enumerate(prenoms):
    print(valeur)

for index, prenom in enumerate(prenoms):
    prenoms[index] = prenom.upper()