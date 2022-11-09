from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    
    pos_item_map = list(map(lambda idx: (arr[idx], idx), range(n)))
    pos_item_map.sort(reverse=True)

    shifts = 0
    ans = []
    def real_pos(x): return (x + shifts) % n

    for (num, pos) in pos_item_map:
        if real_pos(pos) == num - 1:
            ans.append(0)
            continue
        
        shifts -= pos + 1
        ans.append(pos + 1)
    
    ans.reverse()
    print( *ans)