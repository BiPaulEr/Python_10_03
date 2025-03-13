def generateur_test():
    for x in range(0, 2):
        yield x
        print("OK")


for x in generateur_test():
    print(x)
for x in generateur_test():
    print(x)
"""
print(next(generateur_test_iterable))
print(next(generateur_test_iterable))
print(next(generateur_test_iterable))
print(next(generateur_test_iterable))
print(next(generateur_test_iterable))
print(next(generateur_test_iterable))
print(next(generateur_test_iterable))
"""