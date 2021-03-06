from linked_list import LinkedList
from node import Node
import pytest

linked_list = LinkedList()
values = [2, 4, 6]
for el in values:
    linked_list.insert(el)


def test_ll_kth_from_end_middle():
    assert 4 == linked_list.ll_kth_from_end(1)

def test_ll_kth_from_end_end():
    assert 2 == linked_list.ll_kth_from_end(0)

def test_ll_kth_from_end_head():
    assert 6 == linked_list.ll_kth_from_end(2)

def test_ll_kth_from_end_same_length():
    assert 'Exception' == linked_list.ll_kth_from_end(3)

def test_ll_kth_from_end_negative():
    assert 'Negative k is not valid' == linked_list.ll_kth_from_end(-1)

def test_ill_kth_from_end_size_one():
    linked_list_one = LinkedList()
    values = [6]
    for el in values:
        linked_list_one.insert(el)
    assert 'Exception' == linked_list_one.ll_kth_from_end(1)

def test_ill_kth_from_end_size_one2():
    linked_list_one = LinkedList()
    values = [6]
    for el in values:
        linked_list_one.insert(el)
    assert 6 == linked_list_one.ll_kth_from_end(0)

@pytest.mark.skip('pending')
def test_ill_kth_from_end_empty():
    linked_list_one = LinkedList()
    values = [ ]
    for el in values:
        linked_list_one.insert(el)
    assert 'Exception' == linked_list_one.ll_kth_from_end(1)



@pytest.fixture()
def empty_list():
    linked_list = LinkedList()
    values = [2, 4, 6]
    for el in values:
        linked_list.insert(el)
    return linked_list

