from tree import BinaryTree, BinarySearchTree

'''
BinaryTree connection test
'''

def test_binary_tree_instance():
    tree = BinaryTree()
    assert tree._root is None

'''
add one member happy feet test
'''
def test_add_one_member():
    tree = BinarySearchTree()
    tree.add('james_bond')
    assert tree._root.value == 'james_bond'

'''
add values more than one happy feet test
'''
def test_add_three_member():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
   
    assert tree._root.value == 6
    assert tree._root.left.value == 5
    assert tree._root.right.value == 7

'''
add values make unballanced tree negative values edge case
'''
def test_add_four_member_unbalance():
    tree = BinarySearchTree()
    tree.add(-6)
    tree.add(8)
    tree.add(7)
    tree.add(-7)

    assert tree._root.value == -6
    assert tree._root.left.value == -7
    assert tree._root.right.value == 8
    assert tree._root.right.left.value == 7
'''
pre order happy feet test
'''
def test_pre_order():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(7)
    tree.add(4)
    tree.add(9)
    tree.add(3)

    expected = [6,4,3,8,7,9]
    actual = tree.pre_order()
    assert expected == actual

'''
in order happy feet test
'''
def test_in_order():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(7)
    tree.add(4)
    tree.add(9)
    tree.add(3)

    expected = [3,4,6,7,8,9]
    actual = tree.in_order()
    assert expected == actual

'''
post order happy feet test
'''
def test_post_order():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(7)
    tree.add(4)
    tree.add(9)
    tree.add(3)

    expected = [3,4,7,9,8,6]
    actual = tree.post_order()
    assert expected == actual
'''
contains only has not root happy feet test
'''
def test_contains_one_false():
    tree = BinarySearchTree()
    tree.add(8)
    expected = False
    actual = tree.contains(6)
    assert expected == actual
'''
contains only has root happy feet test
'''
def test_contains_one_True():
    tree = BinarySearchTree()
    tree.add(8)
    expected = True
    actual = tree.contains(8)
    assert expected == actual

'''
contains right side True happy feet test
'''
def test_contains_big_True():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(7)
    tree.add(4)
    tree.add(9)
    tree.add(3)
    expected = True
    actual = tree.contains(9)
    assert expected == actual
'''
contains right side False happy feet test
'''
def test_contains_big_False():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(7)
    tree.add(4)
    tree.add(9)
    tree.add(3)
    expected = False
    actual = tree.contains(15)
    assert expected == actual

'''
contains left side True negative values edge test
'''
def test_contains_small_True():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(-1)
    tree.add(4)
    tree.add(9)
    tree.add(3)
    expected = True
    actual = tree.contains(-1)
    assert expected == actual

'''
contains left side False negative values edge test
'''
def test_contains_small_False():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(-5)
    tree.add(4)
    tree.add(9)
    tree.add(3)
    expected = False
    actual = tree.contains(-15)
    assert expected == actual