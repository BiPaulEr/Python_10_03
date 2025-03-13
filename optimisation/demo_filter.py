prenoms = [5, -5, 89, 62, -3 , 5 , 1, 2 , 3 , 4, 7, 8789, -544944]

prenoms = list(filter(lambda x: x >= 0 and x <= 10, prenoms))
print(prenoms) #TRue -> ['paul', 'ernest', 'martin'] # False -> []
[5, 5, 1, 2, 3, 4, 7]