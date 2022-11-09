from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    print(a, a*2)
