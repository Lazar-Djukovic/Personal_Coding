num = int(input())
words = []

for x in range(num):
  words.append(input())

for i in range(0,num):
  if len(words[i]) > 10:
      words[i] = str(words[i][0]) + str(len(words[i])-2) + str(words[i][len(words[i])-1])

for i in range(num):
  print(words[i])