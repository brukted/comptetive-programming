from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    arr.sort(key=lambda x: x % k)

    i = 0
    j = n - 1

    ans = 0

    while i < j:
        if (arr[i] % k + arr[j] % k) >= k:
            ans += (arr[i] + arr[j]) // k
            i += 1
            j -= 1
        else:
            ans += arr[i] // k
            i += 1

    if i == j:
        ans += (arr[i] // k)
    print(ans)
