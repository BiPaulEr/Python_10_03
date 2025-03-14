def repeat_rep(nombre_repetition):
    def repeat(f):
        def wrapper(*args, **kwargs):
            for x in range (0, nombre_repetition):
                f(*args, **kwargs)
        return wrapper
    return repeat

@repeat_rep(5)
def fonction_simple():
    print("Function simple")

@repeat_rep(2)
def fonction_simple2():
    print("Function simple2")

fonction_simple()

fonction_simple2()