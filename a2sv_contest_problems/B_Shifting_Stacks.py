from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))

    is_valid = all(
        map(lambda i: (sum(arr[:i + 1]) >= ((i * (i + 1)) // 2)), range(n)))

    print("YES" if is_valid else "NO")
