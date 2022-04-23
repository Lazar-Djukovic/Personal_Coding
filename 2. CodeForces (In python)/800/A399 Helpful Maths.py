str = input()
x = str.split("+")
string = ''

x.sort()

for i in range(len(x)):
  string += x[i] + '+'

print(string[:-1])
