from merge_sort import merge_sort


def test_merge_sort_one_element():
    arr = [0]
    merge_sort(arr)
    assert arr == [0]

def test_merge_arr():
    arr = [8,4,23,42,16,15]
    merge_sort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_merge_reverse_order_arr():
    arr = [20, 18, 12, 8, 5, -2]
    merge_sort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

def test_merge_nearly_sorted_arr():
    arr = [2,3,5,7,13,11]
    merge_sort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]

def test_merge_few_uniques_arr():
    arr = [5,12,7,5,5,7]
    merge_sort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

def test_merge_sorted_arr():
    arr = [5, 5, 5, 7, 7, 12]
    merge_sort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]


def test_merge_sort_edge_case():
    arr = [2.5, -5, 0, 8, 7,  9, ]
    merge_sort(arr)
    assert arr == [ -5, 0, 2.5, 7, 8, 9]


def test_merge_sort_edge_case_two():
    arr = ['a', 'c', 'bond', 'b']
    merge_sort(arr)
    assert arr == ['a', 'b', 'bond', 'c', ]

# it does not work string and integers together as below test
# fauilure case test
@pytest.mark.skip('pending')
def test_merge_sort_edge_case_three():
    arr = ['a', 2.5, -5, 0, 'b', 8, 7, 'c', 9, 'bond']
    merge_sort(arr)
    assert arr == ['a', 2.5, -5, 0, 'b', 8, 7, 'c', 9, 'bond']