n = int(input())
current = 0
min = 0

for i in range(n):

  inp = input()
  x = inp.split(' ')

  current -= int(x[0])
  current += int(x[1])
  if current > min:
    min = current

print(min)
  
