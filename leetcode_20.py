'''
Problem 20: Valid Parentheses
Date: 10/04/23
Link: https://leetcode.com/problems/valid-parentheses/
Problem:
    - Check if may proper na kapares na closing bracket yung opening bracket na nasa string 
'''
# Mk 1 attempt
'''
s = "(}{)"

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
                if pairs[s[i]] in s and (s.index(pairs[s[i]]) - i) % 2 > 0 and i < s.index(pairs[s[i]]): # checks if yung closing bracket ay nasa slist
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
'''

# Mk 2 Attempt
s = "()"

def isValid(s):
    pairs = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    
    if len(s) % 2 == 0:
        counter = 0 # counts the number of pairs
        for i in range(len(s)):
            print(i)
            if s[i] in pairs.keys(): # checks if the current symbol is an opening bracket
                if pairs[s[i]] in s and (s.index(pairs[s[i]]) - i) % 2 > 0 and i < s.index(pairs[s[i]]): # checks if yung closing bracket ay nasa list
                    s= s.replace(s[s.index(pairs[s[i]])], "")
                    s = s.replace(s[i], "")
                    print(s)
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
