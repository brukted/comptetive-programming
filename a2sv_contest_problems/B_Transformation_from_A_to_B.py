from collections import deque
from sys import stdin, stdout

a, b = map(int, stdin.readline().split())

queue = deque([(a, 1, [a])])

while queue:
    num, depth, nums = queue.popleft()

    if num == b:
        print("YES")
        print(depth)
        print(*nums)
        exit()

    if num * 10 + 1 <= b:
        n = nums.copy()
        n.append(num * 10 + 1)
        queue.append((num * 10 + 1, depth + 1, n))

    if num * 2 <= b:
        n = nums.copy()
        n.append(num * 2)
        queue.append((num * 2, depth + 1, n))

print("NO")
