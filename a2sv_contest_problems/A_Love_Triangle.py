from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

visited = set()

for num in arr:
    A = num - 1
    B = arr[A] - 1
    C = arr[B] - 1

    if arr[C] - 1 == A:
        print("YES")
        exit()

print("NO")
