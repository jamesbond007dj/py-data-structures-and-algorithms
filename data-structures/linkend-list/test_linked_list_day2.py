from linked_list import LinkedList
from node import Node
import pytest

linked_list = LinkedList()
values = [2, 4, 6]
for el in values:
    linked_list.insert(el)


def test_append_empty():
    linked_list = LinkedList()
    assert "8" == linked_list.append(8)

def test_append():
    assert "6428" == linked_list.append(8)

def test_insert_before(empty_list):
    assert "6842" == empty_list.insert_before(4, 8)

def test_insert_before_none():
    assert 'Value is not in the list' == linked_list.insert_before(7, 8)

def test_insert_after_none():
    assert 'Value is not in the list' == linked_list.insert_before(7, 8)

def test_insert_after(empty_list):
    assert "6842" == empty_list.insert_before(4, 8)

@pytest.fixture()
def empty_list():
    linked_list = LinkedList()
    values = [2, 4, 6]
    for el in values:
        linked_list.insert(el)
    return linked_list

@pytest.fixture()
def empty_list():
    linked_list = LinkedList()
    values = [2, 4, 6]
    for el in values:
        linked_list.insert(el)
    return linked_list