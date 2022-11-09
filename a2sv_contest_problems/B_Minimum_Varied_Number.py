from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    s = int(stdin.readline().strip())
    ans = []
    ss = set()

    while s > 0:
        for i in range(9, 0, -1):
            if i in ss or i > s:
                continue
            s -= i
            ans.append(str(i))
            ss.add(i)
            break

    print("".join(ans[::-1]))
