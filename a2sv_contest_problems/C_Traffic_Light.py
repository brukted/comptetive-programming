from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, c = stdin.readline().strip().split()
    n = int(n)
    s = stdin.readline().strip()

    if c == 'g':
        print(0)
        continue

    ans = 0
    curr_idxs = []
    first = None
    for i in range(n):
        if first == None and s[i] == 'g':
            first = i

        if s[i] == c:
            curr_idxs.append(i)
        elif s[i] == 'g':
            while curr_idxs:
                ans = max(ans, i - curr_idxs.pop())
    
    while curr_idxs:
        ans = max(ans, n - curr_idxs.pop() + first)
    
    print(ans)
