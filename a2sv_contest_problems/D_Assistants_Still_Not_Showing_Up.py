from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

availability = list(
    map(lambda _: tuple(map(int, stdin.readline().split())), range(m)))
availability.sort(key= lambda x: (x[0], -x[1]))

days = availability[0][0]
l, r = availability[0]

for (s, e) in availability[1:]:
    print((s,e), days)
    if s > l:
        days += s - l
        l, r = max(l, min(r + 1, e + 1)), max(r, e)
    else:
        l, r = max(l, min(r + 1, e + 1)), max(r, e)
    
    print(days, (l, r))

days += n - l - 1

print(days)
