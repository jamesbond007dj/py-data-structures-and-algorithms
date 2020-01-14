from insertion_sort import insertion_sort
import pytest

def test_insertion_sort():
	arr = [8, 2, 10, 9, 12]
	expected = [2, 8, 9, 10, 12]
	assert insertion_sort(arr) == expected


def test_insertion_sort_one():
	arr = [8]
	expected = [8]
	assert insertion_sort(arr) == expected

def test_sorted():
    arr = [2,4,5,7,10]
    expected = [2,4,5,7,10]
    assert insertion_sort(arr) == expected

def test_negative():
    arr = [2,4,-5,7,-10]
    expected = [-10,-5,2,4,7]
    assert insertion_sort(arr) == expected

def test_negative_and_point():
    arr = [2,0.4,-5,1.7,-10]
    expected = [-10,-5,0.4,1.7,2]
    assert insertion_sort(arr) == expected