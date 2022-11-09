from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))


arr.sort()
ans = n
j = 1
for i in range(n):
    arr[i] *= -1 if arr[i] < 0 else 1

    for j in range(i + 1, n):
        if arr[j] > 0 and arr[j] > arr[i]:
            arr[j] *= -1
            ans -= 1
            break

print(ans)
