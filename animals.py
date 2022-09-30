from abc import ABC
from abc import abstractmethod

class AnimalNameError(Exception):
    pass

class Animal(ABC):

    INITIAL_WEIGHT = 1

    def __init__(self, name):
        if not name :
            raise AnimalNameError("An animal must have a name")
        self.name = name
        self.weight = self.INITIAL_WEIGHT
    
    @abstractmethod
    def make_noise(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):

    def make_noise(self):
        if self.weight > self.INITIAL_WEIGHT :
            return 'Woof Woof!'
        else :
            return "" #silence. no noise.
    
    def eat(self):
        self.weight += 5

class Cat(Animal):
        
    def make_noise(self):
        if self.weight > self.INITIAL_WEIGHT :
            return 'Meow!'
        else :
            return "" #silence. no noise.

    def eat(self):
        self.weight += 2

class House:
    def __init__(self, animals):
        self.animals = animals