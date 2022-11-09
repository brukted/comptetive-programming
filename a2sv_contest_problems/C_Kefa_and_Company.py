from sys import stdin, stdout

n, d = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, stdin.readline().split())))
arr.sort()

i, j = 0, 0
max_ans = 0
factor_sum = 0
while j < n:
    while j < n and arr[j][0] - arr[i][0] < d:
        factor_sum += arr[j][1]
        j += 1
    
    max_ans = max(max_ans, factor_sum)

    while i <= j < n and arr[j][0] - arr[i][0] >= d:
        factor_sum -= arr[i][1]
        i += 1

print(max_ans)