"""
Problem 7 - From CodeScore-MBPP-ET:  
Write a python function to find the last digit when factorial of a divides factorial of b.
"""


def solution1(a, b):
    difference = b - a
    if difference >= 5:
        return 0
    if difference == 0:
        return 1
    
    last_digit = 1
    for num in range(a + 1, b + 1):
        last_digit = (last_digit * num) % 10
    
    return last_digit