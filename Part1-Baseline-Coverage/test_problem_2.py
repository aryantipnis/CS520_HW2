from Problem_2 import solution1

def test_simple_cases():
    assert solution1('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)" 
    assert solution1('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)" 
    assert solution1('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)" 
    assert solution1('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"  
    assert solution1('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"
    assert solution1('hellomyfriend')=='lippsqcjvmirh', "This prints if this assert fails 2 (good for debugging!)" 
    assert solution1('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "This prints if this assert fails 3 (good for debugging!)"  # Check some edge cases that are easy to work out by hand. assert candidate('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"

