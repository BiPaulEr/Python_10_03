import time

def log(fonction):
    def wrapper(a, b):
        result = fonction(a, b)
        print(f"{fonction.__name__} {a} {b} -> {result}")
        return result
    return wrapper

def cache(fonction):
    dictionnaire = {} 
    def wrapper(a, b):
        if (a, b) in dictionnaire:
            print("Already claculated")
            return dictionnaire[(a, b)]
        print("Need to be claculated")   
        result = fonction(a, b)
        dictionnaire[(a, b)] = result
        print(dictionnaire)
        return result
    return wrapper

@log     
@cache
def fonction_couteuse(a, b):
    time.sleep(3)
    return a + b 

@cache
def fonction_couteuse2(a, b):
    time.sleep(3)
    return a + b 

(fonction_couteuse(1, 2))
(fonction_couteuse(10, 20))
(fonction_couteuse(1, 2))
(fonction_couteuse(10, 20))