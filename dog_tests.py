import pytest 
from dog import Dog

@pytest.fixture(scope="function")
def new_dog():
    return Dog("Jimmy", "Poodle")

def test_dog_name_creation(new_dog):
    assert new_dog.name == "Jimmy"

def test_dog_breed_creation(new_dog):
    assert new_dog.breed == "Poodle"

def test_feed_dog(new_dog):
    weight_before = new_dog.weight
    new_dog.eat()
    assert weight_before + 5 == new_dog.weight