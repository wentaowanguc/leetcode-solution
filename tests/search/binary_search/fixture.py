import pytest


@pytest.fixture
def non_rotated_sorted_array():
    return [1,2,3,4,5,6,7]

@pytest.fixture
def rotated_sorted_array():
    return [12,14,15,3,8,10]

@pytest.fixture
def rotated_sorted_array_with_duplicates():
    return [3,3,1,3]

@pytest.fixture
def non_rotated_sorted_array_with_duplicates():
    return [1,3,3]