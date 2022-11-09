from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
i, j = 0, 0
ans = 0

xs = set()

while j < n:
    while j < n and (arr[j] % k != 0 or arr[j] // k not in xs) and arr[j] not in xs:
        xs.add(arr[j])
        if arr[j] % k == 0:
            xs.add(arr[j] // k)
        j += 1

    ans = max(ans, j - i)

    while i < j < n and not ((arr[j] % k != 0 or arr[j] // k not in xs) and arr[j] not in xs):
        xs.remove(arr[i])
        if arr[i] % k == 0:
            xs.remove(arr[i] // k)
        i += 1

print(ans)
