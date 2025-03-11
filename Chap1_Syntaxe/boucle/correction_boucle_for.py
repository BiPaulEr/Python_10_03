#exerice 1
for i in range(20, 26):
    print(i**2)

#exerice 2
somme = 0
for i in range(1, 51):
    if i%2:
        somme = somme + i
print(somme)

print(sum(range(1, 50, 2)))

#exercie 3
chaine = "Bonjour Python"
for carac in reversed(chaine):
    print(carac)

for index in range(len(chaine)-1, -1, -1):
    print(chaine[index])

for index in range(1, len(chaine)+1):
    print(chaine[len(chaine) - index])

#exercice 4
nombre = int(input("Rentre un nombre entier"))
for i in range (1, 11):
    print("Multiplication ", i, " * ", nombre, " = ", i * nombre)

for nombre in range(1, 11):
    for i in range (1, 11):
        print("Multiplication ", i, " * ", nombre, " = ", i * nombre)

#Exerice 5
liste = range(10, -1, -1)
for index, valeur in enumerate(liste):
    print(index, " -> ", valeur)