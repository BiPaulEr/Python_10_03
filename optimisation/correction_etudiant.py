noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

etudiant = list(zip(noms, scores))
print(etudiant) #[('Alice', 85), ('Bob', 92), ('Charlie', 78)]

etudiant_20 = list( map(lambda x : (x[0], x[1] / 5), etudiant))
print(etudiant_20) #[('Alice', 17.0), ('Bob', 18.4), ('Charlie', 15.6)]

etudiant_sup_17 = list(filter(lambda x : x[1] >= 17, etudiant_20))
print(etudiant_sup_17) #[('Alice', 17.0), ('Bob', 18.4)]

notes = list(map(lambda a : a[1], etudiant_sup_17))
moyenne = sum(notes) / len(notes)
print(moyenne)