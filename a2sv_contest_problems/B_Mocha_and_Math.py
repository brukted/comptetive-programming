from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))

    bit_count = [0] * 33

    for num in arr:
        for shift in range(33):
            bit_count[shift] += 1 if num & 1 << shift else 0

    ans = 0

    for idx, c in enumerate(bit_count):
        if c == n:
            ans |= 1 << idx

    print(ans)
