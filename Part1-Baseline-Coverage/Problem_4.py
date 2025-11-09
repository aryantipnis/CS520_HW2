"""
Problem 4 - From HumanEval/74: 

Write a function that accepts two lists of strings and returns the list that has total number of chars in the all strings of the list less than the other list.  
If the two lists have the same number of chars, return the first list.  

Examples: 
total_match([], []) ➞ [] 
total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi'] 
total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin'] 
total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi'] 
total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
"""


def solution1(list1, list2): 
    sum1 = sum(len(s) for s in list1)
    sum2 = sum(len(s) for s in list2)
    return list1 if sum1 <= sum2 else list2