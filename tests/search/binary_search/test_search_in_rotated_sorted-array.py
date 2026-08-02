from solutions.search.binary_search.search_in_rotated_sorted_array import search
from tests.search.binary_search.fixture import non_rotated_sorted_array, rotated_sorted_array


def test_not_find_in_non_rotated_sorted_array(non_rotated_sorted_array):
    assert search(non_rotated_sorted_array, 8) == -1


def test_find_in_non_rotated_sorted_array(non_rotated_sorted_array):
    assert search(non_rotated_sorted_array, 7) == 6


def test_not_find_in_rotated_sorted_array(rotated_sorted_array):
    assert search(rotated_sorted_array, 4) == -1


def test_find_in_rotated_sorted_array(rotated_sorted_array):
    assert search(rotated_sorted_array, 8) == 4