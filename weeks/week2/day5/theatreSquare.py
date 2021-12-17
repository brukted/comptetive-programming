# https://codeforces.com/problemset/problem/1/A

inp = input()
inp = inp.split()
m = int(inp[0])
n = int(inp[1])
a = int(inp[2])
if m % a == 0:
    x = m // a
else:
    x = m // a + 1
if n % a == 0:
    y = n // a
else:
    y = n // a + 1
print(x * y)


