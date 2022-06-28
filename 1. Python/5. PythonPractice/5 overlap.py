import random
a = []
b = []

for i in range(1,random.randint(5,20)):
  a.append(random.randint(1,100))

for i in range(1,random.randint(5,20)):
  b.append(random.randint(1,100))


overlap = []

for num in a:
  if num in b:
    if num in overlap:
      pass
    else:
      overlap.append(num)

print(a)
print(b)
print(overlap)