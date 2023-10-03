'''
Problem 14: Longest Common Prefix
Date: 10/03/23
Link: https://leetcode.com/problems/longest-common-prefix/
Problem:
    - Write a function to find the longest common prefix string amongst an array of strings
    - If there is no common prefix return an empty string
'''

'''
strs = ["flower", "flamingo", "flakes"]
list_a = [] # list to contain the letters of the first word
list_b = [] # list to contain the letters of the current word that is similar with the letter from the first word
compare = False

for data in strs: # checks for every word
    for letter in data:
        if compare == False: # first word will store all of its letter in list_a
            list_a.append(letter)
        else: # sorting conditions for the second words onwards
            if letter in list_a and data.index(letter) == list_a.index(letter):
                list_b.insert(list_a.index(letter), letter)
            elif letter in list_b and data.index(letter) == list_a.index(letter):
                break
            else:
                continue
            print(f"Current word: {data}")
            print(list_b)
    compare = True # flips the indicator after the first letter

print(list_a)
print(list_b)

'''

# CORRECT SOLUTION 1   

def longestCommonPrefix(strs):
    # for cases na sureball yung sagot sa prefix

    if len(strs) == 0: # if empty yung strs list return empty string
        return("")
    if len(strs) == 1: # if isa lang laman nung strs list return the whole damn thing
        return(strs[0])
    
    # for cases na more than one laman nung strs list

    pref_str = strs[0] # use the first string as the reference string
    pref_len = len(pref_str) # use the length of the reference string as the reference length 

    for s in strs[1:]:

        while pref_str != s[0:pref_len]: # while hindi pa equal yung reference string dun sa current string given the length pref_len
            pref_str = pref_str[0:(pref_len-1)] # bawasan ng isang letter yung pref_str baka magmatch
            pref_len =- 1 # bawasan din yung pref_len baka magmatch

            if pref_len == 0: # if naubos na yung pref_str it means walang common prefix among the strings
                return("")

    return(pref_str) # returns the common prefix kung ano man maging result
