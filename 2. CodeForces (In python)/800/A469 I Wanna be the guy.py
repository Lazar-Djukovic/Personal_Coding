n = int(input())
x = str(input())
y = str(input())

guy = True

i = 1

while i <= n:
  if x.count(str(i)) == 0 and y.count(str(i)) == 0:
    guy = False
  i += 1

if guy == True:
  print("I become the guy.")
elif guy == False:
  print("Oh, my keyboard!")

  