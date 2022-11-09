from collections import deque
import itertools
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
pages = []
letters = set()
for _ in range(n):
    page_no = int(stdin.readline().strip())
    page = []
    for _ in range(k):
        page.append(input())
        letters.update(page[-1])
    pages.append((page_no, page))

pages.sort()
pages = list(map(lambda p: p[1], pages))
arr = list(itertools.chain.from_iterable(pages))
pages = None

graph = {x: [] for x in letters}
in_degree = {x: 0 for x in letters}

for i in range(len(arr) - 1):
    s1, s2 = arr[i], arr[i+1]

    for j in range(len(s1)):
        if j >= len(s2):
            print("IMPOSSIBLE")
            exit()

        if s1[j] != s2[j]:
            graph[s1[j]].append(s2[j])
            in_degree[s2[j]] += 1
            break

starting_nodes = list(filter(lambda x: in_degree[x] == 0, letters))

que = deque(starting_nodes)
order = []

while que:
    letter = que.popleft()
    order.append(letter)

    for nei in graph[letter]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            que.append(nei)

if len(order) != len(letters):
    print("IMPOSSIBLE")
else:
    print(*order, sep='')
