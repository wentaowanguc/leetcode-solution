import pytest
from solutions.sum.two_sum import two_sum_sorting, two_sum_dictionary

class TestTwoSum:
    def __init__(self, nums: list[int], target: int, output: list[int]):
        self.nums = nums
        self.target = target
        self.output = output

@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def single_match_list():
    return TestTwoSum([5,3,1,7],6, [0,2])


@pytest.fixture
def multiple_match_list():
    return TestTwoSum([5,3,1,7],8, [0,1])


@pytest.fixture
def no_match_list():
    return TestTwoSum([5,3,1,7],22, [])


def test_two_sum_dictionary_empty_list(empty_list):
    assert two_sum_dictionary(empty_list, 20) == []


def test_two_sum_dictionary_single_match(single_match_list):
    actual_output = two_sum_dictionary(single_match_list.nums,single_match_list.target).sort()
    expected_output = single_match_list.output.sort()
    assert actual_output == expected_output


def test_two_sum_dictionary_multiple_match(multiple_match_list):
    assert two_sum_dictionary(multiple_match_list.nums,multiple_match_list.target) == multiple_match_list.output


def test_two_sum_dictionary_no_match(no_match_list):
    assert two_sum_dictionary(no_match_list.nums,no_match_list.target) == []


def test_two_sum_sorting_empty_list(empty_list):
    assert two_sum_sorting(empty_list, 20) == []


def test_two_sum_sorting_single_match(single_match_list):
    actual_output = two_sum_sorting(single_match_list.nums,single_match_list.target).sort()
    expected_output = single_match_list.output.sort()
    assert actual_output == expected_output


# def test_two_sum_sorting_multiple_match(multiple_match_list):
#     assert two_sum_sorting(multiple_match_list.nums,multiple_match_list.target) == multiple_match_list.output


def test_two_sum_sorting_no_match(no_match_list):
    assert two_sum_sorting(no_match_list.nums,no_match_list.target) == []