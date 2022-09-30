
from abc import ABC
from abc import abstractmethod

class AnimalNameError(Exception):
    pass

class Animal(ABC):
    
    INITIAL_WEIGHT = 2

    def __init__(self, name):
        if name :
            self.name = name
            self.weight = self.INITIAL_WEIGHT
        else :
            raise AnimalNameError("Animals must be instantiated with a name.")
    
    @abstractmethod
    def make_noise(self):
        pass

    @abstractmethod
    def eat(self):
        pass
        
class Dog(Animal):

    def make_noise(self):
        return "Woof Woof!"

    def eat(self):
        self.weight += 5

class Cat(Animal):

    def make_noise(self):
        return "Meow!"

    def eat(self):
        self.weight += 2

class House:
    def __init__(self, animals):
        self.animals = animals