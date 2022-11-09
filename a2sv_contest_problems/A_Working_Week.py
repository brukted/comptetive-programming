from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    n -= 3

    l1 = 1
    n -= 1

    if n == 2:
        l2 = 1
        n = 1
    elif n == 3:
        l2 = 2
        n = 1
    else:
        l2 = n // 4
        n -= n // 4
    
    # print(l1, l2, n, l1 + l2 + n)

    print(min(int(abs(l1 - l2)), int(abs(l1 - n)), int(abs(l2 - n))))
