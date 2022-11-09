from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

summ = sum(arr[:k])
best = (summ, 1)

for i in range(k, n):
    summ -= arr[i - k]
    summ += arr[i]
    best = min(best, (summ, i - k + 2))

print(best[1])
