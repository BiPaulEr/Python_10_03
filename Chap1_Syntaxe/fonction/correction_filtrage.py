import copy

liste_a_nettoye =  [5, 15, None, 10, 20]
liste_a_nettoye2 =  [5, 15, None, 10, 20]

def nettoyer_donnee(liste):
    new_liste = []
    for element in liste:
        if element != None:
            new_liste.append(element)
    return new_liste

def nettoyer_donnee2(liste):
    new_liste = copy.deepcopy(liste)
    while None in new_liste:
        new_liste.remove(None)
    return new_liste

def filter_donnee(liste):
    new_liste = []
    for element in liste:
        if element >= 0 and element <= 10:
            new_liste.append(element)
    return new_liste

def analyser_donne(liste):
    return filter_donnee(nettoyer_donnee(liste))

liste_sans_none = nettoyer_donnee(liste_a_nettoye)
liste_filtre = filter_donnee(liste_sans_none)
liste_annalyse = analyser_donne(liste_a_nettoye2)


print(liste_a_nettoye) #[5, 15, None, 10, 20]
print(liste_sans_none) #[5, 15, 10, 20]
print(liste_filtre) #[5, 10]
print(liste_annalyse) #[5, 10]
