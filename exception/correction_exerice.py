def check_type_deco(liste):
    def check_type(function):
        def wrapper(*args, **kwargs):
            if len(liste) != len(args):
                raise ValueError(f"liste {liste} not same legth as args {args}")
            for type_value, value in zip(liste, args):
                if not isinstance(value, type_value):
                    raise TypeError("Chaine is not a str ! !")
            return function(*args, **kwargs)
        return wrapper
    return check_type

@check_type_deco([str, int, float])
def test(a,  b, c):
    pass 

test("", 3, 3.5)
test("", 3, 3)

@check_type_deco([str])
def convertir_en_entier(chaine):
    try:
        result = int(chaine)
        return result
    except ValueError as ve:
        print(f"Conversion avortée : {ve}")
        return None
    finally: 
        print("QUOI")
    

print(convertir_en_entier("3"))


print(convertir_en_entier("3.5"))
try:
    a = 3
    print(convertir_en_entier({}))
except TypeError as te:
    pass

class TailleInvalideException(Exception):
    pass

def verifer_taille(chaine):
    if len(chaine) < 5:
        raise TailleInvalideException("")
    
verifer_taille("  ")