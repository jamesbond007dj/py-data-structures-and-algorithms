from ll_merge import LinkedList, Node
from ll_merge import merge_lists
import pytest





def test_ll_merge_first_one_long_list():
    linked_list_one = LinkedList()
    values_one = [1, 2, 3, 5, 7, 9]
    for el in values_one:
        linked_list_one.insert(el)
    
    linked_list_two = LinkedList()
    values_two = [4, 6, 8]
    for el in values_two:
        linked_list_two.insert(el)

    actual = merge_lists(linked_list_one, linked_list_two)

    assert '9 - 8 - 7 - 6 - 5 - 4 - 3 - 2 - 1 - None' == str(actual)


def test_ll_merge_one_first_one_short_list():
    linked_list_one = LinkedList()
    values_one = [1, 2, 3, 5, 7, 9]
    for el in values_one:
        linked_list_one.insert(el)
    
    linked_list_two = LinkedList()
    values_two = [4, 6, 8]
    for el in values_two:
        linked_list_two.insert(el)

    actual = merge_lists(linked_list_two, linked_list_one)
    assert '8 - 9 - 6 - 7 - 4 - 5 - 3 - 2 - 1 - None' == str(actual)

def test_ll_merge_one_string_and_intiger():
    linked_list_one = LinkedList()
    values_one = [1, 2, 3, 5, 7, 9]
    for el in values_one:
        linked_list_one.insert(el)
    
    linked_list_two = LinkedList()
    values_two = [4, 6, 'f']
    for el in values_two:
        linked_list_two.insert(el)

    actual = merge_lists(linked_list_two, linked_list_one)
    assert 'f - 9 - 6 - 7 - 4 - 5 - 3 - 2 - 1 - None' == str(actual)

def test_ll_merge_second_one_empty():
    linked_list_one = LinkedList()
    values_one = [1, 2, 3, 5, 7, 9]
    for el in values_one:
        linked_list_one.insert(el)
    
    linked_list_two = LinkedList()
    values_two = [ ]
    for el in values_two:
        linked_list_two.insert(el)

    actual = merge_lists(linked_list_one, linked_list_two)

    assert '9 - 7 - 5 - 3 - 2 - 1 - None' == str(actual)

def test_ll_merge_first_one_empty():
    linked_list_one = LinkedList()
    values_one = [ ]
    for el in values_one:
        linked_list_one.insert(el)
    
    linked_list_two = LinkedList()
    values_two = [4, 6, 8]
    for el in values_two:
        linked_list_two.insert(el)

    actual = merge_lists(linked_list_one, linked_list_two)

    assert 'None' == str(actual)


