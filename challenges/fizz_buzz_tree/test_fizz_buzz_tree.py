import pytest
from fizz_buzz_tree import Node , BinaryTree , BinarySearchTree , fizz_buzz_tree

def test_tree_instance():
    tree = BinaryTree()
    assert tree.root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree.root.value == 'apples'

@pytest.fixture()
def value_tree():
    tree = BinaryTree()
    tree.add(9)
    tree.add(7)
    tree.add(2)
    tree.add(3)
    tree.add(15)
    tree.add(42)
    tree.add(5)
    tree.add(4)
    tree.add(45)
    tree.add(6)
    tree.add(12)
    return tree

def test_fizz_buzz_tree(value_tree):
    fizz_buzz_tree(value_tree)
    assert value_tree.root.value == 9
    assert value_tree.root.left.left.value == 2
    assert value_tree.root.right.left.value == 12
    assert value_tree.root.right.right.right.value == 45

def test_fizz_buzz_tree_2(value_tree):
    fizz_buzz_tree(value_tree)
    assert value_tree.root.value == 9
    assert value_tree.root.left.left.value == 2
    assert value_tree.root.right.left.value == 12
    assert value_tree.root.right.right.right.value == 45

def test_one_value(value_tree):
    value_tree.root = Node(9)
    expected = fizz_buzz_tree(9)
    assert value_tree.root.value == expected