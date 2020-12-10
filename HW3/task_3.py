def swap (a, b):
    print (f'Your values are {a} and {b}')
    a, b = b, a
    print (F'After swaping they are {a} and {b}')
    return (a, b)

while True:
    a = input('Please, enter your 1-st value: ', )
    b = input('Please, enter your 2-nd value: ', )
    swap(a, b)