produits = [
    {'name': 'yaourt', 'stocks': 80, 'prix': 100.0},
    {'name': 'lait', 'stocks': 90, 'prix': 50},
    {'name': 'oeufs', 'stocks': 100, 'prix': 20},
]
    
produits_prix = sum(map(lambda x: x["stocks"]*x["prix"], produits))

print(sum([x["stocks"]*x["prix"] for x in produits]))

print(produits_prix)
