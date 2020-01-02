import pytest
from find_max_value import _Node , BinaryTree, BinarySearchTree, Queue

"""
Basic Tests
"""

def test_binery_tree():
  assert BinaryTree()

def test_queue():
  assert Queue()

'''
add one member happy feet test
'''
def test_add_one_member():
    tree = BinaryTree()
    tree.add('james_bond')
    assert tree._root.value == 'james_bond'

'''
testing max function
'''
def test_find_max_three_value():
    new_tree = BinaryTree()
    expected = 6
    new_tree.add(2)
    new_tree.add(6)
    new_tree.add(4)
    assert new_tree.find_max_value() == expected

def test_find_max_five_value():
    new_tree = BinaryTree()
    expected = 11
    new_tree.add(3)
    new_tree.add(11)
    new_tree.add(5)
    new_tree.add(11)
    new_tree.add(3)
    assert new_tree.find_max_value() == expected

'''
testing max function edge cases
'''
def test_breadth_first_negative_value():
    new_tree = BinaryTree()
    expected = 119
    new_tree.add(3)
    new_tree.add(119)
    new_tree.add(1)
    new_tree.add(85)
    new_tree.add(-11)
    new_tree.add(-19)
    new_tree.add(19)
    assert new_tree.find_max_value() == expected