from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

last_day = -1
l_idx = 0

availability = list(
    map(lambda _: tuple(map(int, stdin.readline().split())), range(m)))
availability.sort()

for (l, s) in availability:
    if l <= last_day + 1:
        last_day = max(last_day, s)
    else:
        print('YES')
        exit()

if last_day < n - 1:
    print('YES')
else:
    print('NO')
