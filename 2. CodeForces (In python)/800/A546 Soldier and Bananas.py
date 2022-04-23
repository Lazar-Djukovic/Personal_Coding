string = input()
n = string.split(" ")

cost = 0
money = int(n[1])

for i in range(1, (int(n[2])+1)):
  banana = int(n[0]) * i
  cost = cost + banana

borrow = cost - money
if borrow > 0:
  print(borrow)

else:
  print(0)
