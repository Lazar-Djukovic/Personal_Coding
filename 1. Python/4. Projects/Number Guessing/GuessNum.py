import random

run = True

number = random.randint(1,1000)
guesses = 0

print("> Guess the random number beweeen 1 and 1000: ")

while run == True:
  guess = int(input())

  if guess == number:
    print("> Thats the right answer, the number was " + str(number))
    print('')
    print("> It took you " + str(guesses) + " Tries to guess the number")
    run = False

  else:
    if guess < number:
      print("> The number is higher than " + str(guess))
      guesses += 1

    if guess > number:
      print("> The number is less than " + str(guess))
      guesses += 1
  
  print('')
  print('> please enther another number')