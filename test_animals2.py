# A house may have any number of pets living in it. The two possible
# types of pets that can live in a house are dogs and cats. Each dog or cat
# has a name. An animal’s house is its one and only home. You can tell an
# animal to make noise and it will do it in its own way.

# Req clarification (better scoping): Animals can be created with any name except empty strings.

# New req: Animals gain weight every time they eat. Dogs gain 5 units while cats gain 2. 
# Animals start with a default of weight of 1 unit

import pytest
from animals2 import Dog
from animals2 import Cat
from animals2 import House
from animals2 import AnimalNameError

@pytest.fixture(scope="function")
def new_dog():
    return Dog("Ringo")

@pytest.fixture(scope="function")
def new_cat():
    return Cat("George")

def test_dog_creation(new_dog):
    assert new_dog.name == "Ringo" and new_dog.weight == new_dog.INITIAL_WEIGHT

def test_cat_creation(new_cat):
    assert new_cat.name == "George" and new_cat.weight == new_cat.INITIAL_WEIGHT

def test_dog_noise(new_dog):
    assert new_dog.make_noise() == "Woof Woof!"

def test_cat_noise(new_cat):
    assert new_cat.make_noise() == "Meow!"

def test_house_creation(new_dog, new_cat):
    new_house = House([new_dog, new_cat])
    assert new_house.animals == [new_dog, new_cat]

def test_animals_noname():
    with pytest.raises(AnimalNameError):
        dog = Dog("")

def test_dog_eats(new_dog):
    weight_before = new_dog.weight
    new_dog.eat()
    assert new_dog.weight == weight_before + 5 ## initial weight (which is 1) plus 5 

def test_cat_eats(new_cat):
    weight_before = new_cat.weight
    new_cat.eat()
    assert new_cat.weight == weight_before + 2 ## initial weight (which is 1) plus 2 