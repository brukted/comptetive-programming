from collections import defaultdict, deque


t = int(input())

for _ in range(t):
    input()
    n, k = map(int, input().split())
    rooms = list(map(int, input().split()))
    tree = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    visited = set(rooms)
    visited.add(1)

    que = deque(list(map(lambda x: (x, True), rooms)) + [(1, False)])

    can_win = False

    while que:
        r, is_friend = que.popleft()

        for nei in tree[r]:
            if nei not in visited:
                if (not is_friend) and len(tree[nei]) == 1:
                    can_win = True
                    break
                visited.add(nei)
                que.append((nei, is_friend))

    if can_win:
        print('YES')
    else:
        print('NO')
