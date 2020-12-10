# using module math
import math
print(math.factorial(int(input('Please, enter non-negative integer: ', ))))

# using while
num = int(input('Please, enter non-negative integer: ', ))
factorial = 1

while num > 1:
    factorial *= num
    num -= 1

print(factorial)

# using for
number = int(input('Please, non-negative integer: ', ))
fac = 1

for i in range(2, number+1):
    fac *= i

print(fac)