from ll_merge import LinkedList, Node
from ll_merge import merge_lists
import pytest

linked_list_one = LinkedList()
values_one = [1, 2, 3, 5, 7, 9]
for el in values_one:
    linked_list_one.insert(el)
    


linked_list_two = LinkedList()
values_two = [4, 6, 'f']
for el in values_two:
    linked_list_two.insert(el)
    



def test_ll_merge_one():
    actual = merge_lists(linked_list_one, linked_list_two)
    assert "9 - f - 7 - 6 - 5 - 4 - 3 - 2 - 1 - None" == __repr__(actual)

# def test_ll_kth_from_end_end():
#     assert 2 == linked_list.ll_kth_from_end(0)

# def test_ll_kth_from_end_head():
#     assert 6 == linked_list.ll_kth_from_end(2)

# def test_ll_kth_from_end_same_length():
#     assert 'Exception' == linked_list.ll_kth_from_end(3)

# def test_ll_kth_from_end_negative():
#     assert 'Negative k is not valid' == linked_list.ll_kth_from_end(-1)

# def test_ill_kth_from_end_size_one():
#     linked_list_one = LinkedList()
#     values = [6]
#     for el in values:
#         linked_list_one.insert(el)
#     assert 'Exception' == linked_list_one.ll_kth_from_end(1)

# def test_ill_kth_from_end_size_one2():
#     linked_list_one = LinkedList()
#     values = [6]
#     for el in values:
#         linked_list_one.insert(el)
#     assert 6 == linked_list_one.ll_kth_from_end(0)

# @pytest.mark.skip('pending')
# def test_ill_kth_from_end_empty():
#     linked_list_one = LinkedList()
#     values = [ ]
#     for el in values:
#         linked_list_one.insert(el)
#     assert 'Exception' == linked_list_one.ll_kth_from_end(1)



@pytest.fixture()
def empty_list_one():
    linked_list_one = LinkedList()
    values_one = [1, 2, 3, 5, 7, 9]
    for el in values_one:
        linked_list_one.insert(el)
        return linked_list_one

@pytest.fixture()
def empty_list_two():
    linked_list_two = LinkedList()
    values_two = [4, 6, 8]
    for el in values_two:
        linked_list_two.insert(el)
        return linked_list_two