import pytest
from breadth_first import _Node , BinaryTree , BinarySearchTree , Queue



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
testing breadth_first function
'''
# def test_breadth_first_three_value():
#     new_tree = BinaryTree()
#     expected = [2,6,4]
#     new_tree.add(2)
#     new_tree.add(6)
#     new_tree.add(4)
#     assert new_tree.breadth_first() == expected

# def test_breadth_first_eight_value():
#     new_tree = BinaryTree()
#     expected = [2,6,4,2,6,5,2,3]
#     new_tree.add(2)
#     new_tree.add(6)
#     new_tree.add(5)
#     new_tree.add(2)
#     new_tree.add(3)
#     assert new_tree.breadth_first() == expected

