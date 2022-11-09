from sys import stdin, stdout


n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

dp_b = 0
dp_s = 0

for i in range(n - 1, -1, -1):
    dp_b, dp_s = max(dp_b, dp_s - arr[i]), max(dp_s, arr[i] + dp_b)


max_b = dp_b
max_s = dp_s

for i in range(n - 1, -1, -1):
    max_b, max_s = max(
        (max_b, dp_b, -arr[i] + max_s)), max((max_s, dp_s, arr[i] + max_b))

print(max_b)
