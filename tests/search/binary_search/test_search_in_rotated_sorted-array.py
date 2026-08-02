from solutions.search.binary_search.search_in_rotated_sorted_array import search
import pytest

@pytest.fixture
def non_rotated_sorted_array():
    return [1,2,3,4,5,6,7]

@pytest.fixture
def rotated_sorted_array():
    return [12,14,15,3,8,10]

def test_not_find_in_non_rotated_sorted_array(non_rotated_sorted_array):
    assert search(non_rotated_sorted_array, 8) == -1


def test_find_in_non_rotated_sorted_array(non_rotated_sorted_array):
    assert search(non_rotated_sorted_array, 7) == 6


def test_not_find_in_rotated_sorted_array(rotated_sorted_array):
    assert search(rotated_sorted_array, 4) == -1


def test_find_in_rotated_sorted_array(rotated_sorted_array):
    assert search(rotated_sorted_array, 8) == 4