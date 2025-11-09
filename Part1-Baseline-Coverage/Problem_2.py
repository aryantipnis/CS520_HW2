"""
Problem 2 - From HumanEval/89: 
Create a function encrypt that takes a string as an argument and returns a string encrypted with the alphabet being rotated.  
The alphabet should be rotated in a manner such that the letters  shift down by two multiplied to two places. 

For example: 
encrypt('hi') returns 'lm' 

encrypt('asdfghjkl') returns 'ewhjklnop' 

encrypt('gf') returns 'kj' 

encrypt('et') returns 'ix'
"""

def solution1(s):
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            offset = ord('a')
            result.append(chr((ord(ch) - offset + 4) % 26 + offset))
        elif 'A' <= ch <= 'Z':
            offset = ord('A')
            result.append(chr((ord(ch) - offset + 4) % 26 + offset))
        else:
            result.append(ch)
    return ''.join(result)