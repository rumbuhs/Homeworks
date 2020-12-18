import hw7_t1_calculator

while True:
    shape = input('Please, enter the name of shape, you want to find a square: ', )
    shape = shape.upper()
    if shape == "RECTANGLE": 
        a = int(input("Please, enter rectangle's length: ")) 
        b = int(input("Please, enter rectangle's breadth: "))
        print(hw7_t1_calculator.rectangle(a, b))
    elif shape == 'TRIANGLE':
        c = int(input("Please, enter triangle's height length: ")) 
        d = int(input("Please, enter triangle's breadth length: ")) 
        print(hw7_t1_calculator.triangle(c, d))
    elif shape == 'CIRCLE':
        r = int(input("Please, enter circle's radius length: ")) 
        print(hw7_t1_calculator.circle(r))
    else: 
        print("Sorry! Chose betwen rectangle, triangle or circle")
