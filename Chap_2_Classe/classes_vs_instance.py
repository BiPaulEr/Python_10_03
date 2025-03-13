class Person():
    nom_famille = "martin"

    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age

    def presente(self, fort = False):
        msg = self.prenom + " " + self.nom_famille + " " + str(self.age)
        if (fort):
            msg = msg.upper()
        print(msg)


print(Person.nom_famille)

simp1 = Person("paul", 18)

simp1.presente()

print(simp1.nom_famille)


simp2 = Person("ernest", 90)
simp2.presente(fort = True)
simp3 = Person("normal", 8)

print(type(simp1))
print(type(simp2))

print(simp1)

print(simp2)

print("end")