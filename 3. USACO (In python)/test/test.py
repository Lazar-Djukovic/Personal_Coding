"""
ID: bdimitr1
LANG: PYTHON3
TASK: test
"""
import pathlib

fin = open (pathlib.Path(__file__).parent.resolve() / 'test.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'test.out', 'w')

x,y = [int(_) for _ in fin.readline().strip().split()]

sum = x+y
fout.write (str(sum) + '\n')
fout.close()