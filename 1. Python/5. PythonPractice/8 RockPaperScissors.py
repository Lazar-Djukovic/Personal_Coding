import random
a = ['rock','paper','scissors']
done = False

while done == False:
  print('welcome to rock,paper,scissors, please enter your choice: ')
  choice = str(input('> '))
  computer = a[random.randint(0,2)]
  if choice == 