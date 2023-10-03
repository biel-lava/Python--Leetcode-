'''
Problem 13: Roman to Integers (part I)
Date: 09/12/23
Link: https://leetcode.com/problems/roman-to-integer/
Problem:
    - Create a function that converts the roman numeral into integer
    - may cases na if may naunang smaller roman numeral minus ang function
'''

test_case = ["iv", "ix", "xl", "xc", "cd", "cm", "MCMXCIV", "dcxxi"]

def roman_converter(roman_number):
    equiv = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    sum = 0
    prev_num = " "
    for current_num in roman_number.upper():
        if current_num in ["X", "V", "L", "C", "D", "M"]:
                if prev_num in ["I"]:
                    if sum < 2:
                        sum = equiv[current_num] - equiv[prev_num]
                    else:
                        sum += equiv[current_num] - 2 
                elif prev_num in ["X", "C"]:
                    sum += equiv[current_num] - equiv[prev_num] - equiv[prev_num]
                else:
                    sum += equiv[current_num]
        else:
            sum += equiv[current_num]  
        prev_num = current_num
    
    print(f"Roman number: {roman_number.upper()}   Equivalent: {sum} \n") 

for roman in test_case:
    roman_converter(roman)


# CORRECT SOLUTION 1
'''
def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans

'''

''''
# CORRECT SOLUTION 2

def romanToInt(s):
        roman_table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # reverse iteration solution

        sum = 0 # tracks the current total of the sum 
        last = "I" # tracks the current letter

        for numeral in s[::-1]: # starts going through the string from the last letter
            if roman_table[numeral] < roman_table[last]: # for instances na mas maliit yung value ng current letter relative dun sa previous letter (for example sa "IV" in reverse mas maliit yung I compared sa V)
                sum -= roman_table[numeral]
            else:
                sum += roman_table[numeral]
            last = numeral
        return sum
        
print(romanToInt("MCMXCIV"))
'''


