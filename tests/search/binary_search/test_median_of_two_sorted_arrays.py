from solutions.search.binary_search.median_of_two_sorted_arrays import findMedianSortedArrays

import pytest

@pytest.fixture
def empty_array():
    return []

@pytest.fixture
def sorted_array_1():
    return [1,2]

@pytest.fixture
def sorted_array_2():
    return [3,4]

@pytest.fixture
def sorted_array_3():
    return [2]

def test_median_of_two_sorted_arrays_empty_array(empty_array, sorted_array_1):
    assert findMedianSortedArrays(empty_array, sorted_array_1) == 1.5

def test_median_of_two_sorted_arrays_even_size(sorted_array_1, sorted_array_2):
    assert findMedianSortedArrays(sorted_array_1, sorted_array_2) == 2.5

def test_median_of_two_sorted_arrays_odd_size(sorted_array_1, sorted_array_3):
    assert findMedianSortedArrays(sorted_array_1, sorted_array_3) == 2.0