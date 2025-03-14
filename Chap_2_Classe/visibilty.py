class Personne():
    def __init__(self, nom):
        self.__nom = nom
        self.__prenom = "Paul"

    def saluer(self):
        print("Bonjour ", self.__nom)


persone1 = Personne("Nom1")
persone1.saluer()
print(dir(persone1))
#print(persone1.__nom)
print(persone1._Personne__nom)