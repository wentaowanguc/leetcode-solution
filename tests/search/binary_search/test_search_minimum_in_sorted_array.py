from solutions.search.binary_search.search_minimun_in_sorted_array import search
from tests.search.binary_search.fixture import non_rotated_sorted_array, non_rotated_sorted_array_with_duplicates, rotated_sorted_array, rotated_sorted_array_with_duplicates


def test_search_minimum_in_non_rotated_sorted_array(non_rotated_sorted_array):
    assert search(non_rotated_sorted_array) == 1

def test_search_minimum_in_rotaed_sorted_array(rotated_sorted_array):
    assert search(rotated_sorted_array) == 3

def test_search_minimum_in_non_rotated_sorted_array_with_duplcates(non_rotated_sorted_array_with_duplicates):
    assert search(non_rotated_sorted_array_with_duplicates) == 1

def test_search_minimum_in_rotated_sorted_array_with_duplicates(rotated_sorted_array_with_duplicates):
    assert search(rotated_sorted_array_with_duplicates) == 1
    
