t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    sim = sum(arr)

    if sim < s:
        print("-1")
        continue

    if sim == s:
        print("0")
        continue

    b = list(filter(lambda x: arr[x] == 1, range(n)))

    diff = sim - s

    best = min(n - b[len(b) - diff], b[diff - 1] + 1)

    j = len(b) - diff
    i = -1

    for _ in range(diff - 1):
        i += 1
        j += 1

        nb = n - b[j] + b[i] + 1
        best = min(best, nb)

    print(best)
