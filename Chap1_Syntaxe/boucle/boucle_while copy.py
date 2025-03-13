def function(liste):
    liste.clear()
    if not liste:
        return None
    if len(liste) == 1:
        return liste[0]
    
    minimum = liste[0]
    for element in liste[1:]:
        if element < minimum:
            minimum = element
    return minimum   

liste1 = []
liste2 = [1]
liste3 = [-1, 3, 4, -6]

print(function(liste1))
print(function(liste2))
print(function(liste3))

print(liste3)