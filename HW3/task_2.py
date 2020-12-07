while True:
    try:
        num = int(input('Please, enter four-digit natural number: '))
        if len(str(num)) == 4:
            break
        else:
            print ('To continue, you need to enter only four-digit natural number')
    except ValueError:
        print('Oops! That was no valid number. Please, try again')

# finding produckt of number
num_list = list(str(num))
num_product = int(num_list[0]) * int(num_list[1]) * int(num_list[2]) * int(num_list[3])
print (f'The product of the digits of your number {num} is', num_product)

# finding revese of number 
num_rev = int(str(num)[::-1])
print (f'The reverse of your number {num} is', num_rev)

# sorting the number
num_list.sort()
num_sort = int(''.join(num_list))
print(f'Your number {num} in sorted order is {num_sort}')