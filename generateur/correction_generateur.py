def nombres_pair(n):
    for i in range(0, n, 2):
        yield i

for i in nombres_pair(5):
    print(i)

pair = (x for x in range(0, 50, 2))
for i in pair:
    print(i)

def nombres_carre(n):
    for i in range(1, n):
        yield i**2

for i in nombres_carre(5):
    print(i)

def fibonacci(n):
    yield 0
    a, b = 0, 1
    for _ in range(0, n-1):
        yield b
        a, b = b, a+b

print("FIBO")
for i in fibonacci(60):
    print(i)

