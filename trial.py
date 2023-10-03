def oddNumbers(l, r):
    for num in range(l, r+1):
        if num % 2 == 0:
            continue
        else:
            print(num) 
        

oddNumbers(3, 9)

