strs = ["flower", "flamingo", "flakes"]
list_a = [] # list to contain the letters of the first word
list_b = [] # list to contain the letters of the current word that is similar with the letter from the first word
compare = False

for data in strs: # checks for every word
    for letter in data:
        if compare == False: # first word will store all of its letter in list_a
            list_a.append(letter)
        else:
            if letter in list_a and data.index(letter) == list_a.index(letter):
                list_b.append(letter)
            else:
                continue
    compare = True # flips the indicator after the first letter

print(list_a)
print(list_b)
        