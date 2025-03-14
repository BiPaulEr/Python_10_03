class Banque():
    def __init__(self):
        self.__compte = 1000

    def __operation(self, montant):
        self.__compte = self.__compte + montant

    def depot(self, montant):
        if (montant > 0):
            self.__operation(montant)

banque = Banque()
#print(banque.__compte)
#banque.__operation(12)
print(banque._Banque__compte)
banque._Banque__operation(-500)
print(banque._Banque__compte)