"""
Problem 3 - From HumanEval/84: 

Given a positive integer N, return the total sum of its digits in binary.  
Example: 
For N = 1000, the sum of digits will be 1 the output should be "1". 

For N = 150, the sum of digits will be 6 the output should be "110". 

For N = 147, the sum of digits will be 12 the output should be "1100".  

Variables: @N integer 
Constraints: 0 ≤ N ≤ 10000. 
Output: a string of binary number. 
"""

"""
Solution after introducting a small bug 
"""

def solution1(N):
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
    if N < 0:
        raise ValueError("N must be non-negative")
    
    total = 0
    n = N
    if n == 0:
        return 0
    else:
        while n > 0:
            total += n % 10
            n //= 10
    
    return format(total, 'b')