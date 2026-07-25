import pytest

from solutions.palindrome_number.is_palindrome_number import is_palindrome_mathmatics, is_palindrome_string_slicing

@pytest.fixture
def negative_number():
    return -121


@pytest.fixture
def zero():
    return 0


@pytest.fixture
def single_digit_palindrome_number():
    return 3


@pytest.fixture
def palindrome_number():
    return 102201


@pytest.fixture
def non_palindrome_number():
    return 123


def test_is_palindrome_mathmatics_negative(negative_number):
    assert not is_palindrome_mathmatics(negative_number)


def test_is_palindrome_mathmatics_zero(zero):
    assert is_palindrome_mathmatics(zero)


def test_is_palindrome_mathmatices_single_digit(single_digit_palindrome_number):
    assert is_palindrome_mathmatics(single_digit_palindrome_number)


def test_is_palindrome_mathmatics_palindrome(palindrome_number):
    assert is_palindrome_mathmatics(palindrome_number)


def test_is_palindrome_mathmatics_non_palindrome(non_palindrome_number):
    assert not is_palindrome_mathmatics(non_palindrome_number)


def test_is_palindrome_string_slicing_negative(negative_number):
    assert not is_palindrome_string_slicing(negative_number)


def test_is_palindrome_string_slicing_zero(zero):
    assert is_palindrome_string_slicing(zero)


def test_is_palindrome_string_slicing_single_digit(single_digit_palindrome_number):
    assert is_palindrome_string_slicing(single_digit_palindrome_number)


def test_is_palindrome_string_slicing_palindrome(palindrome_number):
    assert is_palindrome_string_slicing(palindrome_number)


def test_is_palindrome_string_slicing_non_palindrome(non_palindrome_number):
    assert not is_palindrome_string_slicing(non_palindrome_number)