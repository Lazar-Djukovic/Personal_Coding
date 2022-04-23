# The program pulls a text document into a program, counts the number of words, /
# puts them into a dictionary, counts the number of times each word occurs, /
# And calculates the memory saving of the algrorithm

# Opens and reads the text file
f = open("test.txt", "r")
text = f.read()

# Splitting it by spaces
AllWords = text.split(" ")

#Closing the .txt file
f.close()

# Word counter
def CountWords(list):
  return(len(list))

def occurance(word, dictionary, AllWords):
  count = 1
  for i in AllWords:
    if i == word and len(i) > 1:
      count += 1
  
  if word in dictionary:
    pass

  else:
    dictionary.append(word)

  if count == 1:
    print("The word " + str(word) + " occurs 1 time.")
  else:
    print("The word " + str(word) + " occurs " + str(count) + " times.")

#def byte(list):
  #total = 0
  #for word in list:
    #total = total + bytes(word)
  #return(total)

#Dictionary list
dictionary = []


print("----------------------------")
#Making a dictionary which contains no duplicates
for word in AllWords:
  if word in dictionary:
    pass
  #Makes the word lowercase so they all match.
  else:
    word = word.lower()
    occurance(word, dictionary,AllWords)  
    


print("----------------------------")
print("The total amount of words is: " + str(CountWords(AllWords)))
print("----------------------------")
print("Here is the dictionary without repeated words: ")
print("The total amount of words in the dictionary is: " + str(CountWords(dictionary)))
print("----------------------------")
#print("The text takes up " + byte(AllWords))
##print("The memory saving of the dictionary algorithm is: ")