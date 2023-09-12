'''
Problem 13: Roman to Integers (part I)
Date: 09/12/23
Link: https://leetcode.com/problems/roman-to-integer/
Problem:
    - 
'''

roman_num = input("\nEnter roman numeral: ")
equiv = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
sum = 0
prev_num = ""

for current_num in roman_num.upper():
    print(f"\nPrevious number: {prev_num}")
    print(f"Current number: {current_num}")  
    if current_num in ["X", "V", "L", "C", "D", "M"]:
            if prev_num in ["I", "X", "C"]:
                sum += equiv[current_num] - equiv[prev_num] #- equiv[prev_num]
                #sum += current_sum
    else:
        sum += equiv[current_num]
    print(f"Current sum: {sum}\n")    
    prev_num = current_num
    
print(sum) 
