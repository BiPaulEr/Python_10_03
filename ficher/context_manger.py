class ContextManager:
    def __enter__(self):
        print("Entre ds le contexte")
        return "CEST LOBJET"
    
    def __exit__(self, exc_type, exc_instance, traceback):
        if (exc_type):
            print(f"{exc_instance}")
        else:
            print("Pas dexception")
        print("Sortir du contexte")
        return True
    
with ContextManager() as object_prepare_dans_le_enter:
    print(object_prepare_dans_le_enter)
    print("Je suis dans le contexte")
    raise Exception("QUOI")
