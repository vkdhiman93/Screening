# Write a program for multiple inhertitance

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('Eating')


class Mammal(Animal):
    def walk(self):
        print('Walking')


class WingedAnimal(Animal):
    def fly(self):
        print('Flying')


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Animal))
# object class is the base class of all classes in python
print(isinstance(m, object))
issubclass(Mammal, Animal)
issubclass(Mammal, object)
