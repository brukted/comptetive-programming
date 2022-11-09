from collections import defaultdict
from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

if n < 3:
    print(0)
    exit()

x = sum(arr) - arr[0]

prefix_sum = [0] * n
prefix_count = defaultdict(int)

prefix_count[arr[0]] = 1
prefix_sum[0] = arr[0]

ans = 0

for i in range(1, n):
    if prefix_sum[i - 1] == x * 2:
        ans += prefix_count[x]

        if prefix_sum[i - 1] == x:
            ans -= 1

    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    prefix_count[prefix_sum[i]] += 1

    x -= arr[i]

# print(x, prefix_count, prefix_sum, sep='\n')
print(ans)
