class Personne():
    def __init__(self, nom, prenom):
        self.nom_nom = nom
        self.prenom = prenom

    def saluer(self):
        print("Bonjour ", self.nom_nom, " ", self.prenom)


persone1 = Personne("Prenom1", "Nom1")
print(persone1.nom_nom)
persone1.nom_nom = '"luguurt'
persone1.saluer()

personne2 = Personne("Oui", "Oui")
personne2.saluer()