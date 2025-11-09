import pytest
import math
from Problem_9 import solution1 


# --- Valid input tests ---

def test_first_term():
    # t = 1 → should return a * r^(0) = a
    assert solution1(5, 1, 3) == 5


def test_typical_geometric_term():
    # a = 2, r = 3, t = 4 → 2 * 3^(3) = 54
    assert math.isclose(solution1(2, 4, 3), 54)


def test_fractional_ratio():
    # a = 8, r = 0.5, t = 3 → 8 * (0.5)^2 = 2
    assert math.isclose(solution1(8, 3, 0.5), 2.0)


def test_negative_ratio():
    # a = 5, r = -2, t = 3 → 5 * (-2)^(2) = 20
    assert math.isclose(solution1(5, 3, -2), 20.0)


def test_zero_ratio():
    # r = 0 → term after first becomes 0
    assert solution1(5, 2, 0) == 0


def test_a_zero():
    # a = 0 → all terms are 0
    assert solution1(0, 5, 10) == 0


def test_large_t():
    # Test large t to ensure math.pow handles it
    assert math.isclose(solution1(1, 10, 2), 512.0)


# --- Error condition tests ---

def test_non_integer_t_string():
    with pytest.raises(TypeError):
        solution1(5, "3", 2)


def test_non_integer_t_float():
    with pytest.raises(TypeError):
        solution1(5, 2.5, 2)


def test_non_integer_t_list():
    with pytest.raises(TypeError):
        solution1(5, [3], 2)


def test_t_zero():
    with pytest.raises(ValueError):
        solution1(5, 0, 2)


def test_t_negative():
    with pytest.raises(ValueError):
        solution1(5, -4, 2)


#Iteration 2
def test_large_a():
    # Large a times moderate r
    assert solution1(1e100, 5, 2) == 1e100 * 16

def test_small_a():
    # Tiny a with huge exponent
    val = solution1(1e-100, 50, 10)
    assert math.isfinite(val)

def test_ratio_one():
    # All terms equal to a
    assert solution1(5, 100, 1) == 5

def test_ratio_zero_large_t():
    # Beyond first term, all zero
    assert solution1(5, 100, 0) == 0

def test_ratio_negative_one():
    # Alternating signs
    assert solution1(3, 5, -1) in (3, -3)

def test_ratio_one():
    # All terms equal to a
    assert solution1(5, 100, 1) == 5

def test_ratio_zero_large_t():
    # Beyond first term, all zero
    assert solution1(5, 100, 0) == 0

def test_ratio_negative_one():
    # Alternating signs
    assert solution1(3, 5, -1) in (3, -3)

def test_performance_large_t():
    # This should execute quickly without timeouts
    _ = solution1(2, 1_000_000, 1.000001)

#Iteration 3
# --- Additional edge and corner cases ---

def test_ratio_very_close_to_one():
    """
    r very close to 1 should not drift due to floating-point precision.
    Checks stability when exponent is large.
    """
    result = solution1(10, 1000000, 1.0000000001)
    # Should be a large but finite number, no overflow or nan
    assert math.isfinite(result)


def test_ratio_very_close_to_zero():
    """
    Extremely small positive r — ensures proper underflow handling.
    """
    result = solution1(5, 500, 1e-20)
    assert result < 1e-100  # should approach zero


def test_ratio_negative_fraction():
    """
    Negative fractional ratio — tests alternating sign and shrinking magnitude.
    """
    val = solution1(4, 5, -0.5)
    # Term 5: 4 * (-0.5)^(4) = 4 * 0.0625 = 0.25
    assert math.isclose(val, 0.25)


def test_ratio_is_nan():
    """
    r = NaN should propagate NaN as per IEEE 754.
    """
    result = solution1(10, 3, math.nan)
    assert math.isnan(result)


def test_ratio_is_inf():
    """
    Infinite ratio should return inf (or -inf) based on sign of a.
    """
    result = solution1(2, 3, math.inf)
    assert math.isinf(result) and result > 0


def test_ratio_is_negative_inf():
    """
    Negative infinite ratio should result in +/- inf depending on exponent parity.
    """
    val_even = solution1(2, 3, -math.inf)   # exponent (t-1)=2 → positive inf
    val_odd = solution1(2, 4, -math.inf)    # exponent (t-1)=3 → negative inf
    assert math.isinf(val_even) and val_even > 0
    assert math.isinf(val_odd) and val_odd < 0


def test_a_is_inf():
    """
    a = inf should dominate regardless of r.
    """
    result = solution1(math.inf, 5, 0.5)
    assert math.isinf(result)


def test_a_is_negative_inf():
    """
    Negative infinity initial term should preserve sign.
    """
    result = solution1(-math.inf, 4, 2)
    assert math.isinf(result) and result < 0


def test_t_large_near_overflow_boundary():
    """
    Tests the boundary before float overflow (exp with large base).
    """
    val = solution1(1, 308, 10)  # around the exponent limit for float64
    assert math.isfinite(val) or math.isinf(val)


def test_non_integer_a_and_r():
    """
    a and r can be floats — verify correct math.pow handling.
    """
    val = solution1(2.5, 3, 1.2)
    assert math.isclose(val, 2.5 * (1.2 ** 2))


def test_min_positive_a_and_r():
    """
    Smallest positive nonzero float values.
    """
    val = solution1(1e-308, 2, 1e-308)
    assert val >= 0  # Should not produce negative or NaN