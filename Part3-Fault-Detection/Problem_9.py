"""
Problem 9 - From CodeScore-MBPP-ET:
Write a function to find t-nth term of geometric series.

"""

"""
Solution after introducting a small bug 
"""

import math

def solution1(a, t, r):
    if not isinstance(t, int):
        raise TypeError("t must be an integer (1-based index)")
    if t < 1:
        raise ValueError("t must be >= 1")
    return a * (math.pow(r, t + 1))