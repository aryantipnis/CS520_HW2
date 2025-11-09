from Problem_3 import solution1

def test_simple_cases():
    assert solution1(1000) == "1", "Error"
    assert solution1(150) == "110", "Error"
    assert solution1(147) == "1100", "Error"
    
    # Edge cases
    assert solution1(333) == "1001", "Error"
    assert solution1(963) == "10010", "Error"