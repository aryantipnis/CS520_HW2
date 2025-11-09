from Problem_4 import solution1

def test_simple_cases():  
    # Check some simple cases 
    assert solution1([], []) == [] 
    assert solution1(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi'] 
    assert solution1(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin'] 
    assert solution1(['4'], ['1', '2', '3', '4', '5']) == ['4'] 
    assert solution1(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi'] 
    assert solution1(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi'] 
    assert solution1(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']   
    
    # Check some edge cases that are easy to work out by hand. 
    assert solution1([], ['this']) == [] 
    assert solution1(['this'], []) == [] 