from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))

    twos = 0

    for num in arr:
        two_pow, curr = 1, 2

        while curr <= num and num % curr == 0:
            curr *= 2
            two_pow += 1

        twos += two_pow - 1

    if twos >= n:
        print(0)
        continue

    poss = []
    two_pow, curr = 32, 2 ** 32

    while curr > 0:
        poss.append((two_pow, (n // curr) - (n // (curr * 2))))
        curr //= 2
        two_pow -= 1

    ans = cum = 0
    # print(poss, disc, twos, n)

    for (two_pow, cnt) in poss:
        while cnt > 0 and twos < n:
            twos += two_pow
            ans += 1
            cnt -= 1

        if twos >= n:
            break

    if twos < n:
        print(-1)
    else:
        print(ans)
