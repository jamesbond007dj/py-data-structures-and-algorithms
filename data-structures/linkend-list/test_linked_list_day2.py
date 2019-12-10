from linked_list import LinkedList
from node import Node

linked_list = LinkedList()
values = [2, 4, 6]
for el in values:
    linked_list.insert(el)


def test_append_empty():
    linked_list = LinkedList()
    assert "8" == linked_list.append(8)

def test_append():
    assert "2, 4, 6, 8" == linked_list.append(8)

def test_insert_before():
    assert "2, 8, 4, 6" == linked_list.insert_before(4, 8)

def test_insert_before_none():
    assert 'Value is not in the list' == linked_list.insert_before(7, 8)

def test_insert_after_none():
    assert 'Value is not in the list' == linked_list.insert_before(7, 8)

def test_insert_after():
    assert "2, 4, 8, 6" == linked_list.insert_before(4, 8)