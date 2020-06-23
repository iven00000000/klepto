class Parent:
    def __new__(cls, val):
        return super(Parent, cls).__new__(cls)

    def __init__(self, val):
        self.val = val + 1

class Child(Parent):
    def __new__(cls, val):
        return super(Child, cls).__new__(cls, val)

    def __init__(self, val):
        self.val += 1

c = Child(1)
print(c)
print(c.val)