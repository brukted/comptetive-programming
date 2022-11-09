from sys import stdin, stdout

n, t = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

i, j = 0, 0
ans = 0

while j < n:
    while j < n and arr[j] <= t:
        t -= arr[j]
        j += 1

    ans = max(ans, j - i)

    while i <= j < n and arr[j] > t:
        t += arr[i]
        i += 1

print(ans)
