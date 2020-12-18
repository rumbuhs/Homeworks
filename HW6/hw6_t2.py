from math import pi
from math import sqrt

def calculator(shape):
    """
    This funktion will find the
    square of a rectangle, triangle or circle.
    depending on the user's choice.
    Input: name of shape
    Otput: the square of the shape
    """
    shape = shape.upper()
    if shape == "RECTANGLE": 
        a = int(input("Please, enter rectangle's length: ")) 
        b = int(input("Please, enter rectangle's breadth: "))
        print ((a*b), ' is a rectangle square') 

    elif shape == 'TRIANGLE':
        c = int(input("Please, enter triangle's height length: ")) 
        d = int(input("Please, enter triangle's breadth length: ")) 
        print ((0.5*d*c), 'is a triangle square')

    elif shape == 'CIRCLE':
        r = int(input("Please, enter circle's radius length: ")) 
        print((sqrt(r)*pi), 'is a circle square') 
    else: 
        print("Sorry! Chose betwen rectangle, triangle or circle")

while True:
    shape = input('Please, enter the name of shape, you want to find a square: ', )
    calculator(shape)