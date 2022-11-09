from sys import stdin, stdout

n = int(stdin.readline().strip())

curr = 0
ss = set()

for _ in range(n):
    ch, num = stdin.readline().strip().split()
    num = int(num)

    if ch == '-':
        if num in ss:
            ss.remove(num)
        else:
            curr += 1
    else:
        ss.add(num)
        curr = max(curr, len(ss))

print(curr)
