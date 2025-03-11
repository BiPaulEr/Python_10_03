prenoms = ["paul", "ernest", "martin"]

print(list(enumerate(prenoms)))
#[('paul', 'Dupont'), ('ernest', 'Aigouy'), ('martin', 'Lefebvre')]

for index, prenom in enumerate(prenoms):
    prenoms[index] = prenom.upper()