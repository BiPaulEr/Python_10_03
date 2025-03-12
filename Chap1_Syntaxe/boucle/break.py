elements = [0, None, 0.0, True, 0, 7]  # True et 7 évaluent à True
trouve = False
element_a_trouve = None
for element in elements:
    print(f'analyse de l’élément {element}')
    if element == element_a_trouve:
        trouve = True
        break
if trouve:
    print('Au moins un élément évalue à True')
else:
    print('Tous les éléments évaluent à False')

