from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    input()
    n, k = map(int, input().split())
    rooms = list(map(int, input().split()))
    vlad_tree = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        vlad_tree[u].append(v)
        vlad_tree[v].append(u)

    friends_tree = defaultdict(int)

    # root the tree
    queue = deque([(1, -1)])
    while queue:
        node, parent = queue.popleft()
        friends_tree[node] = parent

        if parent in vlad_tree[node]:
            vlad_tree[node].remove(parent)

        for nei in vlad_tree[node]:
            queue.append((nei, node))

    friends = k
    friend_visited = set(rooms)
    vlad_visited = {1}

    que = deque(list(map(lambda x: (x, True), rooms)) + [(1, False)])

    can_win = False

    while que and not can_win:
        node, is_friend = que.popleft()

        if is_friend:
            if friends_tree[node] in vlad_visited:
                continue

            if friends_tree[node] in friend_visited:
                friends -= 1
                continue

            friend_visited.add(friends_tree[node])
            que.append((friends_tree[node], True))

        else:
            for nei in vlad_tree[node]:
                if nei in friend_visited:
                    continue

                if len(vlad_tree[nei]) == 0:
                    can_win = True
                    break

                que.append((nei, False))
                vlad_visited.add(nei)

    if can_win:
        print('-1')
    else:
        print(friends)
