class Compteur:
    def __init__(self):
        self.begin = 10

    def __iter__(self):
        return CompteurState()

class CompteurState:
    def __init__(self):
        self.begin = 10

    def __next__(self):
        self.begin = self.begin - 1
        if (self.begin < 0):
            raise StopIteration
        return self.begin + 1
    
compteur = Compteur()

for i in compteur:
    print(i)
for i in compteur:
    print(i)