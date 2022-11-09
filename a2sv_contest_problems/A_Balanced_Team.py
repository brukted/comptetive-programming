from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

arr.sort()
i = 0
j = 0
max_size = 0

while j < len(arr):
    while j < len(arr) and arr[j] - arr[i] <= 5:
        j += 1

    max_size = max(max_size, j - i)

    while j < len(arr) and i <= j and arr[j] - arr[i] > 5:
        i += 1

print(max_size)
