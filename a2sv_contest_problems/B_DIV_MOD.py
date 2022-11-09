from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    l, r, a = map(int, stdin.readline().split())
    ans1 = r // a + r % a

    if l <= (r // a - 1) * a + a - 1:
        ans1 = max(ans1, (r // a) + a - 2)

    print(ans1)
