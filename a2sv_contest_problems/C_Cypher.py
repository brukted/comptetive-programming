t = int(input())

for _ in range(t):
    n = int(input())
    final = list(map(int, input().split()))

    for i in range(n):
        moves = input().split()[1]
        net = 0
        for move in moves:
            if move == 'U':
                net -= 1
            else:
                net += 1
        final[i] += net
        final[i] %= 10

    print(' '.join(map(str, final)))
