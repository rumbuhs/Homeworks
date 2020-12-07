while True:
    a = int(input('Please, enter your 1-st number: ', ))
    b = int(input('Please, enter your 2-nd number: ', ))
    highest = max(a, b)
    lowest = min(a, b)
    if a==b:
        print ('Your numbers are equal')
    else:
        print ('Your highest number is: ', highest)
        print ('Your lowest number is: ', lowest)