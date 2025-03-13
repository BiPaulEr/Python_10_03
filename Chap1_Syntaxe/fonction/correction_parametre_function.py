def afficher_prix_total(prix_entree, prix_plat, *prix_supplementaires, prix_dessert = 10, **details_commande):
    prix_total = prix_entree + prix_plat + prix_dessert + sum(prix_supplementaires)
    print("prix total ", prix_total)
    for cle, valeur in details_commande.items():
        print(cle, "->", valeur)


afficher_prix_total(5, 10, 5)
afficher_prix_total(5, 10)
prix_commande = (5, 7, 9)
afficher_prix_total(5, 10, *prix_commande, prix_dessert=50)

details_command_arg = {"client":'John Doe', "table":5, "alergie":'sans gluten'}
afficher_prix_total(5, 10, *prix_commande, prix_dessert=50, **details_command_arg)
