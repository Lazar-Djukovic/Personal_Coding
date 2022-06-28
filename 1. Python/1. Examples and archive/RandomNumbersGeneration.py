k = 19
c = 51
m = 100
x0 = 25

numbers = []
numbers.append(x0)

for i in range(0,30):
  n = ((k*numbers[i])+c) % m
  numbers.append(n)

print(numbers)