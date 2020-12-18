n = int(input('please, enter you number ', ))
f_n = [0, 1]
for i in range (2, n):
    f_n.append(f_n[i-1]+f_n[i-2])
    if f_n==i:
        break
print('Fibonacci list till your number ', f_n)