#exerice 1
compteur = 10
while compteur >= 0:
    print(compteur)
    compteur = compteur -1

#exerice 2
nombres = [15, 20, 25]
index = 0
while index < len(nombres) and nombres[index] < 50:
    index= index+1

if (index < len(nombres)):
    print(nombres[index])

#exerice 3
mdp = ""
while mdp != "Python2024":
    mdp = input("Mot de passe ? ")
print("OUI enfin")

#exerice 4
nombre = int(input("NOMbre ?"))
somme = 0
index = 1
while index <= nombre:
    somme = somme + index
    index = index + 1
print(somme)
