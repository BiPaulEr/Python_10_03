prenoms = ["paul", "ernest", "martin"]
noms = ["Dupont", "Aigouy", "Lefebvre"]

print(list(zip(prenoms, noms)))
#[('paul', 'Dupont'), ('ernest', 'Aigouy'), ('martin', 'Lefebvre')]

for prenom, nom in zip(prenoms, noms):
    print(prenom, nom)