# using list.append
numbers = [x*x for x in range (1, 7)]
flt_numbers = []

for n in numbers:
    flt_numbers.append(float(n))

print (numbers)
print (flt_numbers)

# using list comprehension
my_numbers = [x*x for x in range (2, 9)]
flt_num = [float(n) for n in my_numbers]

print (my_numbers)
print (flt_num)