class Animals:
    def __init__(self):
        print("this is animal class")

class Pets(Animals):
    def __init__(self):
        print("this is pets class")

class Dog(Pets):
    def __init__(self):
        print("this is dog class")

    def bark(self):
        print("bow bow")

d=Dog()
d.bark()
