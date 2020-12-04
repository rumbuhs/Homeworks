name = input('What is your name? ' )
while True:
    try:
        age = int(input('How old are you? ' ))
        break
    except ValueError:
        print('Oops! That was no valid age. Please, enter your age in numbers!')
city = input('Where do you live? ' )


print(f'Hello, {name}! Your age is {age}. You live in {city}')