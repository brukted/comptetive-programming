t = int(input())

for _ in range(t):
    n ,current_ram = list(map(int,input().split()))
    cost_idx_val = [ (val, idx) for idx ,val in enumerate(list(map(int,input().split())))]
    reward = list(map(int,input().split()))
    cost_idx_val.sort()

    for cost , idx in cost_idx_val:
        if cost <= current_ram:
            current_ram += reward[idx]
    print(current_ram)