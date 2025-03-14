import os
print(__file__) #c:\Users\PaulE\Python_10_03\ficher\lecture.py
print(os.path.dirname(__file__)) #c:\Users\PaulE\Python_10_03\ficher
path = os.path.join(os.path.dirname(__file__), "test", "fichier.txt")

with open(path) as f:
    for line in f.readlines():
        print(line.rstrip())

try :
    file = open(path)
    for line in file.readlines():
        print(line.rstrip())
except Exception as e:
    print("d")
finally:
    file.close()

print("end")