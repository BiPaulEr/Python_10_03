liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [6, 7, 8]

print(list(zip(liste1, liste2)))

print(list(zip(liste1, liste2, liste3)))

def maximum(*args):
    print(args)
    if not args:
        return None 
    if len(args) == 1:
        return args[0]

    maximum_tmp = args[0]
    for element in args[1:]:
        if element > maximum_tmp:
            maximum_tmp = element
    return maximum_tmp

print(maximum())
print(maximum(1))
print(maximum(1, 2, -3 , 5))
