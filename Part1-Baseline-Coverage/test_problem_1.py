from Problem_1 import solution1

def test_simple_cases():
    # Simple cases
    assert solution1([4, 2, 3]) == [2, 1]
    assert solution1([1, 2, 3]) == [2, 1]
    assert solution1([]) == []
    assert solution1([5, 0, 3, 0, 4, 2]) == [0, 1]

def test_edge_cases():
    # Edge cases
    assert solution1([1, 2, 3, 0, 5, 3]) == [0, 3]
    assert solution1([5, 4, 8, 4, 8]) == [4, 1]
    assert solution1([7, 6, 7, 1]) == [6, 1]
    assert solution1([7, 9, 7, 1]) == []