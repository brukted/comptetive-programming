from sys import stdin, stdout

n = int(stdin.readline().strip())

min_path = [list(map(int, stdin.readline().split())) for _ in range(n)]
order = list(map(lambda x: int(x) - 1, stdin.readline().split()))

order.reverse()

ans = []

for idx, k in enumerate(order):
    curr = 0

    for i_idx in range(n):
        i = order[i_idx]

        for j_idx in range(n):
            j = order[j_idx]

            if min_path[i][k] + min_path[k][j] < min_path[i][j]:
                min_path[i][j] = min_path[i][k] + min_path[k][j]

            if i_idx <= idx and j_idx <= idx:
                curr += min_path[i][j]

    ans.append(curr)

print(*ans[::-1])
