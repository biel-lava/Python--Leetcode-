'''
Problem 20: Valid Parentheses
Date: 10/04/23
Link: https://leetcode.com/problems/valid-parentheses/
Problem:
    - Write a function to find the longest common prefix string amongst an array of strings
    - If there is no common prefix return an empty string
'''
s = "{[]}"

def isValid(s):
    pairs = {
        "(":")",
        "[":"}",
        "{":"}"
    }
    if len(s) % 2 == 0:
        for i in range(len(s)): # checks if the current symbol is an opening bracket
            if s[i] in pairs.keys():
                print(s[i])
            else:
                print("closing")
    else: # if odd yung len then obvious na may hindi na closed na parenthesis
        return False

print(isValid(s))