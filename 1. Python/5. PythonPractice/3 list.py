array = [1, 1, 2, 3, 5, 8, 13, 21, 34,4, 55, 89]
newlist = []
n = int(input('enter number: '))

for i in array:
  if i < n:
    newlist.append(i)
  
newlist.sort()
print(newlist)
  