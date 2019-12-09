from linked_list import Linkedlist
import Node
import pytest

def test_empty():
    lst = Linkedlist()
    expected = False
    actual = lst.includes(1)
    assert actual == expected

def test_insert():
    lst = Linkedlist()
    lst.insert(3)
    expected = '3'
    actual = lst.to_string()
    assert actual == expected

def test_true():
    lst = Linkedlist()
    lst.insert(2)
    expected = True
    actual = lst.includes(2)
    assert actual == expected

def test_false():
    lst = Linkedlist()
    lst.insert(2)
    expected = False
    actual = lst.includes(3)
    assert actual == expected

def test_string_of2():
    lst = Linkedlist()
    lst.insert(2)
    lst.insert(3)
    expected = '3 2'
    actual = lst.includes()
    assert actual == expected
