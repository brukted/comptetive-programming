from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    arr.sort()
    
    in_sum = sum(arr)

    mi = arr[0]
