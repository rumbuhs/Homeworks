def max_num (n1, n2):
    """
    This function will return you the largest
    number of two numbers
    Input: n1, n2
    Output: largest num of two
    """

    n_l = [n1,n2]
    return max(n_l)
x = int(input('Please, enter you firt number: '))
y = int(input('Please, enter you second number: '))

a = max_num(x, y)
print ('The largest number of your two numbers is:', a)