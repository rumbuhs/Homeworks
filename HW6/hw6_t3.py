def char(string):
    d = {}
    for n in string:
        keys = d.keys()
        if n in keys:
            d[n] += 1
        else:
            d[n] = 1
    print ('This is the number of characters included in a given string', d)
    return d

string = input('Please, enter you string: ', )
char(string)