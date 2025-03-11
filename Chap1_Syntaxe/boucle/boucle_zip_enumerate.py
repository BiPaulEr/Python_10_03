prenoms = ["paul", "ernest", "martin"]
noms = ["Dupont", "Aigouy", "Lefebvre"]
nationalites = ["espagnol", "francais", "italien"]

print(list(zip(prenoms, noms, nationalites)))
#[('paul', 'Dupont', 'espagnol'), ('ernest', 'Aigouy', 'francais'), ('martin', 'Lefebvre', 'italien')]
print(list(enumerate(zip(prenoms, noms, nationalites))))
#[(0, ('paul', 'Dupont', 'espagnol')), (1, ('ernest', 'Aigouy', 'francais')), (2, ('martin', 'Lefebvre', 'italien'))]

for index, (prenom, nom, nation) in enumerate(zip(prenoms, noms, nationalites)):
    prenoms[index] = prenom.capitalize()
    noms[index] = nom.capitalize()
    nationalites[index] = nation.capitalize()

for prenom, nom, nation in zip(prenoms, noms, nationalites):
    print(prenom, nom, nation)
    
    