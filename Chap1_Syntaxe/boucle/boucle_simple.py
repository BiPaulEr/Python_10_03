liste = ["paul", "ernest", "martin"]
print(list(enumerate(liste)))
 #[(0, 'paul'), (1, 'ernest'), (2, 'martin')]
for index, prenom in enumerate(liste):
    liste[index] = prenom.upper()
print(liste)