oth_num = []
od_num = []
ev_num = []
for i in range (1, 10):
    if i % 2==0:
        ev_num.append(i)
    elif i % 3==0:        
        od_num.append(i)
    else:
        oth_num.append(i)

print(' '.join(map(str, ev_num)), 'are even numbers that divisible by 2')
print(' '.join(map(str, od_num)), 'are odd numbers, which divisible by 3')
print(' '.join(map(str, oth_num)), 'are numbers that not divisible by 2 and 3')