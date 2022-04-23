row = 0
line = 0
temp = 0

for a in range(0,5):
  str = input()

  if str.count('1') > 0:
    if a == 0 or a == 4:
      line += 2
    if a == 1 or a == 3:
      line += 1

    for i in range(0,5):
      x = str.split(' ')
      if x[i] == '1':
        if i == 0 or i == 4:
          row += 2
        if i == 1 or i == 3:
          row += 1


total = row + line
print(total)
