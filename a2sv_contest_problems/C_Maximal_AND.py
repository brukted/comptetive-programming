t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = map(int, input().split())

    bit_count = [0] * 32
    an = (2 ** 32) - 1

    for num in arr:
        an &= num
        i = 0
        while num > 0:
            bit_count[i] += (num & 1)
            num >>= 1
            i += 1
    
    # print(bit_count,an)

    for i in range(30, -1, -1):
        if bit_count[i] == n:
            continue
        elif bit_count[i] + k >= n:
            an |= 2 ** i
            k -= n - bit_count[i]

    # print(bit_count)
    print(an)