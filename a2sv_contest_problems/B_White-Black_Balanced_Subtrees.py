from collections import defaultdict
import sys

sys.setrecursionlimit(4000)

t = int(input())

for _ in range(t):
    n = int(input())
    
    parents = list(map(int, input().split()))
    colors = input()
    children = defaultdict(list)

    for idx, p in enumerate(parents):
        children[p - 1].append(idx + 1)

    balanced_count = 0

    def countSub(node = 0):
        global balanced_count

        wt, bt = 0, 0
        for child in children[node]:
            w , b = countSub(child)
            wt, bt = wt + w, bt + b
        
        if colors[node] == 'W':
            wt += 1
        else:
            bt += 1
        
        if wt == bt:
            balanced_count += 1
        
        return wt, bt
    
    countSub()
    
    print(balanced_count)