import pytest
from array_shift import insert_shift_array

# happy path test1
def test_arr_even():
    arr = [1,2,3,4]
    val = 6

    expected = [1,2,6,3,4]
    actual = insert_shift_array(arr, val)

    assert actual == expected

# happy path test2
def test_arr_odd():
    arr = [1,2,3,4,5]
    val = 6

    expected = [1,2,3,6,4,5]
    actual = insert_shift_array(arr, val)

    assert actual == expected

# edge case test1
def test_arr_single():
    arr = [1]
    val = 6

    expected = [1,6]

    actual = insert_shift_array(arr, val)

    assert actual == expected

# edge case test2
def test_arr_empty():
    arr = []
    val = 6

    expected = [6]
    actual = insert_shift_array(arr, val)

    assert actual == expected

# edge case test3
def test_arr_strings():
    arr = ['a=0', 'b=5']
    val = 6

    expected = ['a=0', 6, 'b=5']
    actual = insert_shift_array(arr, val)

    assert actual == expected

@pytest.mark.skip('pending')
def test_arr_failure():
    arr = [1,2,3,4]
    val = 6

    expected = [1,6,2,3,4]
    actual = insert_shift_array(arr, val)

    assert actual == expected
# above test expected failure test, consciously i put a wrong test so I skip it.
