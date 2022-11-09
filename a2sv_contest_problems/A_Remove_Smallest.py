from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    arr.sort()
    diff = 0
    for i in range(1, n):
        diff = max(diff, arr[i] - arr[i - 1])
    
    if diff > 1:
        print("NO")
    else:
        print("YES")