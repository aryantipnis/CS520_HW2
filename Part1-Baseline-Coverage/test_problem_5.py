from Problem_5 import solution1

def test_simple_cases():
    assert solution1([3, 1, 2, 4, 5]) == [1, 4, 12, 20] 
    assert solution1([1, 2, 3]) == [2, 6] 
    assert solution1([3, 2, 1]) == [2, 2] 
    assert solution1([3, 2, 1, 0, 4]) == [2, 2, 0, 16] 
    assert solution1([1]) == []