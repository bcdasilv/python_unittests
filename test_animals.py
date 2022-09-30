# A house may have any number of pets living in it. The two possible
# types of pets that can live in a house are dogs and cats. Each dog or cat
# has a name. An animal’s house is its one and only home. You can tell an
# animal to make noise and it will do it in its own way.

# New req: Animals gain weight everytime they eat. Dogs gain 5 units while cats gain 2.

# New req: Animals make their own noise only if their weight is above their initial weight.

import pytest
from animals import Dog
from animals import Cat
from animals import House
from animals import AnimalNameError

@pytest.fixture(scope="function")
def new_dog():
    return Dog("Ringo")

@pytest.fixture(scope="function")
def new_cat():
    return Cat("George")

def test_dog_creation(new_dog):
    #dog = Dog("Ringo")
    assert new_dog.name == "Ringo" and new_dog.weight == 1

def test_cat_creation(new_cat):
    # cat = Cat("George")
    assert new_cat.name == "George" and new_cat.weight == 1

def test_dog_noise(new_dog):
    #dog = Dog("Ringo")
    new_dog.weight = new_dog.INITIAL_WEIGHT + 1 #bumping the weight above the initial weight
    assert new_dog.make_noise() == "Woof Woof!"

def test_cat_noise(new_cat):
    #cat = Cat("George")
    new_cat.weight = new_cat.INITIAL_WEIGHT + 1 #bumping the weight above the initial weight
    assert new_cat.make_noise() == "Meow!"

def test_house_creation(new_cat, new_dog):
    house = House([new_cat, new_dog])
    assert house.animals == [new_cat, new_dog]

def test_dog_eating(new_dog):
    new_dog.eat()
    assert new_dog.weight == new_dog.INITIAL_WEIGHT + 5

def test_cat_eating(new_cat):
    new_cat.eat()
    assert new_cat.weight == new_cat.INITIAL_WEIGHT + 2

def test_animal_noname():
    with pytest.raises(AnimalNameError):
        dog = Dog("")

def test_dog_noise_underweight(new_dog):
    assert new_dog.make_noise() == ""

def test_cat_noise_underweight(new_cat):
    assert new_cat.make_noise() == ""