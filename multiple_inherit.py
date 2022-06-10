class Employee:
    def greet(self):
        print("Hello, I am an employee")


class Person:
    def greet(self):
        print("Hello, I am a person")


class Manager(Employee, Person):
    pass
# Things gets complicated when when this classes have things in common like greet method here.


class Flyer:
    def fly(self):
        print("I can fly")


class Swimmer:
    def swim(self):
        print("I can swim")


class FlyingFish(Flyer, Swimmer):
    pass


print(FlyingFish.mro())
