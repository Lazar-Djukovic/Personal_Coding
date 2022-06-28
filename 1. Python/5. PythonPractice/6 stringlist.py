string = str(input('Enter a word: '))
list = []
pali = ''

for letter in string:
  list.append(letter)

for i in range(len(list),0,-1):
  pali = pali + str(list[i-1])

if string == pali:
  print('>This string is a palindrome')
else:
  print('>This string is not a palindrome')
