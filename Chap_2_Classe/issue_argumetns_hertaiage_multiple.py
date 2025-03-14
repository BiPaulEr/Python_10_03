class Base:
    def __init__(self):
        print("Base init")

class A(Base):
    def __init__(self, a_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a_value = a_value
        print(f"A init with value: {a_value}")

class B(Base):
    def __init__(self, b_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b_value = b_value
        print(f"B init with value: {b_value}")

class C(A, B):
    def __init__(self, a_value, b_value, *args, **kwargs):
        super().__init__(a_value, b_value, *args, **kwargs)
        print(f"C init : a_value={self.a_value}, b_value={self.b_value}") #C init : a_value=A, b_value=B

c = C("A", "B")
print("end")