from math import sqrt

numbers = [5, None, None, None,-5, 89, 62, -3 , 5 , 1, 2 , 3 , 4, 7, 8789, -544944]

numbers = list(filter(lambda x: (not (x is None)) and x >= 0, numbers))
print(numbers) #TRue -> ['paul', 'ernest', 'martin'] # False -> []
numbers_square = list(map(lambda x : sqrt(x), numbers))
print(numbers_square)

numbers_square_oneline = list(map(lambda x : sqrt(x), filter(lambda x: (not (x is None)) and x >= 0, numbers)))
print(numbers_square_oneline)


numbers_square_oneline_comprehension = [sqrt(x) for x in numbers if (not (x is None)) and x >= 0]
print(numbers_square_oneline_comprehension)

test = (sqrt(x) for x in numbers if (not (x is None)) and x >= 0)
print(test)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

