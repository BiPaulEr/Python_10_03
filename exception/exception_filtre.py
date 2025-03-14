import random

try:
    if (random.randint(1, 10) < 5):
        raise ArithmeticError()
    print("GOOD")
except Exception as e:
    print("e")
else:
    print("Tout va bien")
finally:
    print("Je suis toujours execute comme louis")