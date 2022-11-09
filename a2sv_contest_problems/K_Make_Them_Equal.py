from math import inf
from sys import stdin, stdout

t = int(stdin.readline().strip())


cost = [inf] * (1000 + 1)
cost[1] = 0

for num in range(2, 1001):
    for smaller_num in range(1, num):
        diff = num - smaller_num

        if smaller_num // diff == 0:
            continue

        if (smaller_num // (smaller_num // diff) == diff):
            cost[num] = min(cost[num], 1 + cost[smaller_num])


for _ in range(t):
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    coins = list(map(int, stdin.readline().split()))
    costs = list(map(cost.__getitem__, arr))

    dp_i_p_1 = [0 for _ in range(min(12 * n, k) + 1)]

    for i in range(n - 1, -1, -1):
        for budget in range(min(12 * n, k), -1, -1):
            if costs[i] <= budget:
                new_bud = budget - costs[i]
                dont_skip = coins[i]
                # skip or dont skip
                if new_bud >= 0:
                    dont_skip += dp_i_p_1[new_bud]
                dp_i_p_1[budget] = max(dp_i_p_1[budget], dont_skip)

    print(max(dp_i_p_1))
