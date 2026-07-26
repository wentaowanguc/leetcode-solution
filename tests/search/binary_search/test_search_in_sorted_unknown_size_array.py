from solutions.search.binary_search import ArrayReader
from solutions.search.binary_search.search_in_sorted_unknown_size_array import search

import pytest

@pytest.fixture
def empty_array():
    return ArrayReader()

@pytest.fixture
def target_array():
    reader = ArrayReader()
    reader.append(1)
    reader.append(3)
    reader.append(7)
    reader.append(7)
    reader.append(15)
    return reader


def test_search_in_unknown_size_empty_array(empty_array):
    assert search(empty_array, 2) == -1


def test_search_in_unknown_size_non_duplicates(target_array):
    assert search(target_array, 3) == 1


def test_search_in_unknown_size_duplicates(target_array):
    assert search(target_array, 7) == 2