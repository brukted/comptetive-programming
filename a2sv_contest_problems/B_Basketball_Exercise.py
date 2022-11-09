from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr2 = list(map(int, stdin.readline().split()))

n1, n2 = 0, 0
ans = 0

for i in range(n - 1, -1, -1):
    n1, n2 = max(n1, arr[i] + n2), max(n2, arr2[i] + n1)
    ans = max(ans, max(n1, n2))

print(ans)
