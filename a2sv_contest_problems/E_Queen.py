n = int(input())

nodes = {}
parent = None

for i in range(1, n + 1):
    nodes[i] = list(map(int, input().split()))
    if nodes[i][0] == -1:
        parent = i

order = []
