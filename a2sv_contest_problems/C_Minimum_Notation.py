import heapq
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    s = input()
    hh = []

    for idx, ss in enumerate(s):
        hh.append((int(ss), 0, idx))

    heapq.heapify(hh)

    ans = []
    modded = False

    while hh:
        ss, modi, idx = heapq.heappop(hh)

        if modi == 0:
            if not ans or ans[-1][1] < idx and not modded:
                ans.append((ss, idx))
                continue
            
            heapq.heappush(hh, (min(ss + 1, 9), modi + 1, idx))

        else:
            modded = True
            ans.append((ss, idx))

    print("".join(map(lambda x: str(x[0]), ans)))