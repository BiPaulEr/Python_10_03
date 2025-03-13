liste = [1, 2, 3, 4, 5]

liste_mapper = list(map(lambda x : x**2, liste))
liste_mapper2 = list(map(lambda x : x**3, liste))
liste_mapper3 = list(map(lambda x : x/2, liste))
liste_mapper4 = list(map(lambda x : x+2, liste))
[1, 4, 9, 16, 25]
[1, 8, 27, 64, 125]
[0.5, 1.0, 1.5, 2.0, 2.5]
[3, 4, 5, 6, 7]
[1, 2, 3, 4, 5]

print(liste_mapper)
print(liste_mapper2)
print(liste_mapper3)
print(liste_mapper4)
print(liste)
