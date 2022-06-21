from subprocess import list2cmdline


n = int(input())
list = range(1,n)
divisors = []

for i in list:
  if n % i == 0:
    divisors.append(i)

print(divisors)