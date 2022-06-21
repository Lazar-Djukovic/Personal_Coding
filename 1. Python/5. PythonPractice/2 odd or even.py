num = int(input('enter number:  '))

if num%4 == 0:
  print('this number is a multiple of 4')
elif num == 0:
  print('zero is neither')
elif num%2 == 1:
  print('odd')
elif num%2 == 0:
  print('even')