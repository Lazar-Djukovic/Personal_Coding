n,m,a = input().split(' ')
n = int(n)
m = int(m)
a = int(a)

def calcside(x,y):
  if x > 1:
    return(x%y)
  else:
    return(0.5)

side1 = calcside(n,a)
side2 = calcside(m,a)

total = int(side1 + side2)
print(total)
