anonyme = lambda x, y, z : x if x < 3 else y + z 

print(anonyme(1,2,3))

def anonyme(x, y, z):
    return x + y + z

print(anonyme(1,2,3))