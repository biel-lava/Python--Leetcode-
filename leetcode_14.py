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
        