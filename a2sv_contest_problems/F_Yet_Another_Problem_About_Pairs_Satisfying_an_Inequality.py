t = int(input())

def lower_bound(arr, item):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < item:
            left = mid + 1
        else:
            right = mid
    
    if left < len(arr) and arr[left] < item:
        left += 1

    return left


for _ in range(t):
    n = int(input())
    pairs = 0

    arr = list(map(int, input().split()))

    filtered = []

    for j in range(n):
        if arr[j] < (j + 1):
            pairs += lower_bound(filtered, arr[j])
            filtered.append(j + 1)

    print(pairs)