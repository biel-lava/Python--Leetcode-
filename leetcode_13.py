'''
Problem 13: Roman to Integers (part I)
Date: 09/12/23
Link: https://leetcode.com/problems/roman-to-integer/
Problem:
    - 
'''
test_case = ["iv", "ix", "xl", "xc", "cd", "cm", "MCMXCIV"]

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
                        sum -= equiv[current_num]  
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
     

'''
roman_num = input("\nEnter roman numeral: ")
equiv = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
sum = 0
prev_num = " "

for current_num in roman_num.upper():
    print(f"Current number: {equiv[current_num]}")  
    if current_num in ["X", "V", "L", "C", "D", "M"]:
            if prev_num in ["I"]:
                if sum < 1:
                    sum = equiv[current_num] - equiv[prev_num]
                else:
                    sum -= equiv[current_num]  
            elif prev_num in ["X", "C"]:
                  sum += equiv[current_num] - equiv[prev_num] - equiv[prev_num]
            else:
                sum += equiv[current_num]
    else:
        sum += equiv[current_num]
    
    print(f"Current sum: {sum}\n")    
    prev_num = current_num
    
print(sum) 

'''