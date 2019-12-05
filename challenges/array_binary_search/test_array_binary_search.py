import pytest
from array_binary_search import binary_search

# happy path test1
def test_arr_key_positive_one():
    lst = [1,2,3,4,6]
    key = 6

    expected = 4
    actual = binary_search (lst, key)

    assert actual == expected

# happy path test2
def test_arr_key_positive_two():
    lst = [1,2,6,4,]
    key = 6

    expected = 2
    actual = binary_search (lst, key)

    assert actual == expected

# happy path test3
def test_arr_key_positive_three():
    lst = [1,2,4,]
    key = 6

    expected = -1
    actual = binary_search (lst, key)

    assert actual == expected

# edge case test1
def test_arr_key_edge_one():
    lst = []
    key = 6

    expected = -1
    actual = binary_search (lst, key)

    assert actual == expected

# fauilure case test
@pytest.mark.skip('pending')
def test_arr_key_fauilure():
    lst = [2,6,4,5,6]
    key = 6

    expected = [1,4]
    actual = binary_search (lst, key)

    assert actual == expected

# above test expected failure test, consciously i put 2 same value in array, there is no rule that same value can not be use second time, however it says sorted.
