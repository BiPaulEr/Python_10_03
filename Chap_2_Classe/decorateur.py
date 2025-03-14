def decorateur(f):
    def wrapper(*args, **kwargs):
        print("JE suis dans le wrapper")
        f(*args, **kwargs)
        print("JE suis dans le wrapper")
    return wrapper

@decorateur
def fonction_simple():
    print("Function simple")

@decorateur
def fonction_arg(arg1):
    print(f"Function {arg1}")

fonction_simple()

fonction_arg("DATA")

@decorateur
def fonction_kwargs(arg2 = " OUI", arg1 = "UOI"):
    print(f"Function {arg1} , {arg2}")

fonction_kwargs(arg1 = "OOOOOOOOOOOOOOOOOOOOOOOOOOOO")