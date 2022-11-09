from sys import stdin, stdout
a, b, c, d = map(int, stdin.readline().split())
r = (1 - a / b) * (1 - c / d)
print((a / b) * (1 / (1 - r)))
