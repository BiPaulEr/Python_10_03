produits = [
    {'name': 'yaourt', 'date_expiration': "aujourdhui", 'prix': 100.0},
    {'name': 'lait', 'date_expiration': "demain", 'prix': 50},
    {'name': 'oeufs', 'date_expiration': "aujourdhui", 'prix': 20},
]
    
produits = list(map(lambda x: {"name": x["name"], "date_expiration" : x["date_expiration"], "prix":x["prix"] /6 }, produits) )
print(produits)
[{'name': 'yaourt', 'date_expiration': 'aujourdhui', 'prix': 16.666666666666668}, {'name': 'lait', 'date_expiration': 'demain', 'prix': 8.333333333333334}, {'name': 'oeufs', 'date_expiration': 'aujourdhui', 'prix': 3.3333333333333335}]

