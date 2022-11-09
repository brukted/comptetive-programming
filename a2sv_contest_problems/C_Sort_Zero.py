t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    zeroed = set()
    last = 0

    for idx in range(1, n):
        curr_1 = arr[idx - 1] if arr[idx - 1] not in zeroed else 0
        curr = arr[idx] if arr[idx] not in zeroed else 0
        
        if curr >= curr_1:
            continue
        else:
            while last < idx:
                zeroed.add(arr[last])
                last += 1
    
    print(len(zeroed))
