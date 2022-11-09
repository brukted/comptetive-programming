from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, s = map(int, stdin.readline().split())

    original = n
    original_d = str(n)

    pow = 1
    while sum(map(int, str(n))) > s:
        n = original + (10 ** pow) - int(original_d[-pow:])
        pow += 1

    print(n - original)
