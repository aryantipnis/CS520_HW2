"""
Problem 10 - Own Programming Problem:

Alex loves movies and maintains a list of negative and/or positive integer ratings for the movies in a collection. 
Alex is getting ready for a film festival and wants to choose some subsequence of movies from the collection to 
bring such that the following conditions are satisfied: 
• The collective sum of their ratings is maximal. 
• Alex must go through the list in order and cannot skip more than one movie in a row. 
In other words, Alex cannot skip over two or more consecutive movies. 

Example 1: 
ratings = [-1, -3, -2], Output = -3 

This must include either the second number or the first and third numbers to get a maximal rating sum of -3. 

Example 2: 
ratings = [-3, 2, 4, -1, -2, - 5], Output = 4

The maximal choices are [2, 4, -2] for a sum of 4.

Example 3: 
ratings = [9, -1, -3, 4, 5], output = 17

Alex picks the bolded items in ratings = [9, -1, -3, 4, 5] to get maximum rating = 9 + -1 + 4 + 5 = 17.

1. Happy Path Test Cases (typical valid inputs)
Test Case 1 - Mixed positives and negatives
ratings = [1, -3, 2, 4, -1, -2, -5]
# Optimal subsequence: [1, 2, 4, -2] → sum = 5

Test Case 2 - All positives
ratings = [1, 2, 3, 4, 5]
# Optimal subsequence: take all → sum = 15

Test Case 3 - Alternating positive/negative
ratings = [1, -2, 3, -1, 5]
# Optimal subsequence: [1, 3, -1, 5] → sum = 8

Test Case 4 - Skipping is necessary
ratings = [2, -10, 4, 3, -1, 5]
# Optimal subsequence: [2, 4, 3, 5] → sum = 14

Test Case 5 - Mixed small positives and negatives
ratings = [4, -1, 2, 5, -1, -3, 1]
# Optimal subsequence: [4, 2, 5, -1, 1] → sum = 11

2. Edge / Boundary Test Cases

Test Case 6 - Single movie
ratings = [10]
# Only one movie → sum = 10

Test Case 7 - Two movies
ratings = [3, 7]
# Can take both → sum = 10

Test Case 8 - All negatives
ratings = [-1, -2, -3, -4, -5]
# Must pick non-consecutive optimally → sum = -6

Test Case 9 - All zeros
ratings = [0, 0, 0, 0]
# Sum is zero regardless of subsequence → sum = 0

3. Additional Happy Path / Examples from Problem Statement
Test Case 10 - Example from problem
ratings = [-3, 2, 4, -1, -2, -5]
# Optimal subsequence: [2, 4, -2] → sum = 4

Test Case 11 - Example from problem
ratings = [9, -1, -3, 4, 5]
# Optimal subsequence: [9, -1, 4, 5] → sum = 17

Test Case 12 - Mixed positives and negatives
ratings = [-1, -3, 4, 5]
# Optimal subsequence: [4, 5] → sum = 9

"""

def solution1(ratings):
    if not ratings:
        return 0
    n = len(ratings)
    if n == 1:
        return ratings[0]


    take_prev = ratings[0] 
    skip1_prev = 0          


    for i in range(1, n):
        r = ratings[i]
        take = max(take_prev, skip1_prev) + r
        skip1 = take_prev 
        take_prev, skip1_prev = take, skip1


    ans = max(take_prev, skip1_prev)
    return ans