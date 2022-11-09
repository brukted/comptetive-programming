from sys import stdin, stdout
from math import gcd

a, b = map(int, stdin.readline().split())
if a == b:
    print(a)
else:
    print(1)
