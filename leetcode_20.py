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
        "[":"]",
        "{":"}"
    }
    
    if len(s) % 2 == 0:
        counter = 0 # counts the number of pairs
        for i in range(len(s)):
            if s[i] in pairs.keys(): # checks if the current symbol is an opening bracket
                if pairs[s[i]] in s:
                    if (s.index(pairs[s[i]]) - i) % 2 > 0:
                        counter += 1
                else:
                    return False            
        if counter == len(s) / 2:
            return True
        else:
            return False

    else: # if odd yung len then obvious na may hindi na closed na parenthesis
        return False
   
print(isValid(s))