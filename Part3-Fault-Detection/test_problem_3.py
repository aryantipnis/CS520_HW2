import pytest
from Problem_3 import solution1

def test_zero_input():
    # Edge case: N == 0 should return "0" since sum of digits = 0
    assert solution1(0) == "0"


def test_single_digit():
    # Simple case: binary of 5 is "101"
    assert solution1(5) == "101"


def test_multiple_digits_no_carry():
    # 150 → 1 + 5 + 0 = 6 → "110"
    assert solution1(150) == "110"


def test_multiple_digits_with_large_sum():
    # 9999 → 9+9+9+9 = 36 → binary "100100"
    assert solution1(9999) == "100100"


def test_input_with_zeros_in_between():
    # 1010 → 1+0+1+0 = 2 → binary "10"
    assert solution1(1010) == "10"


def test_large_input_upper_bound():
    # 10000 → 1+0+0+0+0 = 1 → binary "1"
    assert solution1(10000) == "1"


def test_non_integer_input_string():
    # TypeError expected for string
    with pytest.raises(TypeError):
        solution1("123")


def test_non_integer_input_float():
    # TypeError expected for float
    with pytest.raises(TypeError):
        solution1(12.5)


def test_non_integer_input_list():
    # TypeError expected for list
    with pytest.raises(TypeError):
        solution1([123])


def test_negative_integer():
    # Negative input should raise ValueError
    with pytest.raises(ValueError):
        solution1(-10)

#Iteration 2
def test_powers_of_ten():
    assert solution1(10) == format(1, "b")
    assert solution1(100) == format(1, "b")
    assert solution1(1000) == format(1, "b")

def test_large_sum_binary_output():
    N = int("9999999999")  # 10 nines
    # sum = 90 -> binary "1011010"
    assert solution1(N) == "1011010"

def test_boolean_input():
    # bool is technically a subclass of int in Python
    # should it raise TypeError or treat True as 1?
    assert solution1(True) == "1"  # or decide to disallow bools explicitly

def test_none_input():
    with pytest.raises(TypeError):
        solution1(None)

def test_no_side_effects():
    N = 1234
    before = N
    result = solution1(N)
    assert N == before  # ensure N not modified
    assert result == "1010"

#Iteration 3
def test_input_as_boolean_true_false():
    # bools are subclasses of int in Python, so they pass isinstance(N, int)
    # Check that function behavior is logical (True → 1, False → 0)
    assert solution1(True) == "1"
    assert solution1(False) == "0"


def test_input_with_leading_zeros():
    # Integers like 007 are just 7, but this tests robustness against visual ambiguity
    N = int("007")
    assert solution1(N) == "111"  # sum(7) = 7 → binary "111"


def test_large_number_with_mixed_digits():
    # Mix of large and small digits — stress test digit accumulation
    N = 9876543210
    # sum = 45 → binary "101101"
    assert solution1(N) == "101101"


def test_palindromic_number():
    # Palindromic digits — should have same behavior as any multi-digit number
    N = 12321
    # sum = 9 → "1001"
    assert solution1(N) == "1001"


def test_alternating_even_odd_digits():
    # Alternating even/odd digits checks mod/division correctness
    N = 28462846
    # sum = 40 → binary "101000"
    assert solution1(N) == "101000"


def test_large_number_with_trailing_zeros():
    # Many trailing zeros should not affect sum
    N = 1234000000
    # sum = 10 → binary "1010"
    assert solution1(N) == "1010"


def test_input_as_long_integer_string_converted():
    # Ensure behavior is correct after explicit int conversion from string
    N = int("999000111")
    # sum = 9+9+9+0+0+0+1+1+1 = 30 → binary "11110"
    assert solution1(N) == "11110"


def test_input_as_binary_literal():
    # Binary literal in Python: 0b1010 == 10 decimal
    N = 0b1010
    # sum(10) = 1 → binary "1"
    assert solution1(N) == "1"


def test_large_prime_number():
    # Arbitrary large prime — ensures no assumptions about digit structure
    N = 99991  # prime
    # sum = 9+9+9+9+1 = 37 → binary "100101"
    assert solution1(N) == "100101"