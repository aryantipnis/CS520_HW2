from Problem_10 import solution1

def test_simple_cases():
    assert solution1([1, -3, 2, 4, -1, -2, -5]) == 5
    assert solution1([1, 2, 3, 4, 5]) == 15
    assert solution1([1, -2, 3, -1, 5]) == 9
    assert solution1([2, -10, 4, 3, -1, 5]) == 14
    assert solution1([4, -1, 2, 5, -1, -3, 1]) == 11
    assert solution1([10]) == 10
    assert solution1([3, 7]) == 10
    assert solution1([-1, -2, -3, -4, -5]) == -6
    assert solution1([0, 0, 0, 0]) == 0
    assert solution1([-3, 2, 4, -1, -2, -5]) == 4
    assert solution1([9, -1, -3, 4, 5]) == 17
    assert solution1([-1, -3, 4, 5]) == 8