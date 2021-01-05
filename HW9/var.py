n1 = ['a','b','c','d']
n2 = n1
n3 = n1[:]

n2[0] = 'Alice'
n3[1] = 'Bob'

sum = 0 
for ls in (n1,n2,n3):
    if ls[0]=='Alice':
        sum+=1
    if ls[1] == 'Bob':
        sum+=10
print(sum)