import pytest
from fifo_animal_shelter import FifoAnimalShelter, Animal, Dog, Cat, Node


def test_animal():
    animal = Animal('cat')
    assert animal

def test_animal_not():
    animal = Animal('bird')
    assert animal

def test_cat():
    cat = Cat()
    assert cat


def test_dog():
    dog = Dog()
    assert dog


def test_animal_capital_letter():
    cat = Animal('CAT')
    assert cat