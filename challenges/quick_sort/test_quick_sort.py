from quick_sort import quick_sort

import pytest


def test_quick_sort_one_element():
    arr = [0]
    quick_sort(arr, 0,0)
    assert arr == [0]

def test_quick_arr():
    arr = [8,4,23,42,16,15]
    quick_sort(arr, 0,5)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_quick_reverse_order_arr():
    arr = [20, 18, 12, 8, 5, -2]
    quick_sort(arr, 0,5)
    assert arr == [-2, 5, 8, 12, 18, 20]

def test_merge_nearly_sorted_arr():
    arr = [2,3,5,7,13,11]
    quick_sort(arr, 0,5)
    assert arr == [2, 3, 5, 7, 11, 13]

def test_merge_few_uniques_arr():
    arr = [5,12,7,5,5,7]
    quick_sort(arr, 0,5)
    assert arr == [5, 5, 5, 7, 7, 12]

def test_quick_sorted_arr():
    arr = [5, 5, 5, 7, 7, 12]
    quick_sort(arr, 0,5)
    assert arr == [5, 5, 5, 7, 7, 12]


def test_quick_sort_edge_case():
    arr = [2.5, -5, 0, 8, 7,  9, ]
    quick_sort(arr, 0,5)
    assert arr == [ -5, 0, 2.5, 7, 8, 9]


def test_quick_sort_edge_case_two():
    arr = ['a', 'c', 'bond', '1b']
    quick_sort(arr, 0,3)
    assert arr == ['1b', 'a',  'bond', 'c', ]

