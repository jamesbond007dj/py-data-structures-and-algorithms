import pytest
from fifo_animal_shelter import FifoAnimalShelter, Animal, Dog, Cat, Node, Stack


"""
Animal Class test
"""
def test_animal():
    animal = Animal('cat')
    assert animal

"""
connection test
"""
def test_queue():
  assert FifoAnimalShelter()

"""
Cat Class test
"""
def test_cat():
    cat = Cat()
    assert cat

"""
Dog Class test
"""
def test_dog():
    dog = Dog()
    assert dog


def test_animal_capital_letter():
    cat = Animal('CAT')
    assert cat

