t = int(input())

for _ in range(t):
    jumps =  input()
    
    last_r = -1
    max_diff = float("-inf")

    for idx, ch in enumerate(jumps):
        if ch == 'R':
            max_diff = max(max_diff, idx - last_r)
            last_r = idx

    max_diff =  max(max_diff, len(jumps) - last_r)

    
    print(max_diff)   