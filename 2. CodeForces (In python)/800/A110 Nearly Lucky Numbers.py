n = str(input())
luckynums = 0

for num in n:
  if num == '4' or num == '7':
    luckynums += 1

if luckynums == 7 or luckynums == 4:
  print('YES')
else:
  print('NO')