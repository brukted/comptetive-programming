from sys import stdin, stdout

t = int(stdin.readline().strip())


def solve(i, size, arr):
    if size == 1:
        return 0

    ansl = solve(i, size // 2, arr)
    ansr = solve(i + size // 2, size // 2, arr)
    
    if ansl < 0 or ansr < 0:
        return -1

    if arr[i + size // 2 - 1] <= arr[i + size // 2]:
        return ansl + ansr
    elif arr[i + size - 1] > arr[i]:
        return - 1

    j = i + size // 2
    for dl in range(size // 2):
        arr[i + dl], arr[j + dl] = arr[j + dl], arr[i + dl]
    
    return ansl + ansr + 1


for _ in range(t):
    m = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    print(solve(0, m, arr))
