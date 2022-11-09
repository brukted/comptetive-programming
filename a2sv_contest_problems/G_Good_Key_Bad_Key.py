t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [[0 for _ in range(32)] for _ in range(n)]

    def half_not_half(i=0, halves=0):
        if halves == 32 or i == n:
            return 0

        not_half = (arr[i] >> halves) + half_not_half(i + 1, halves) - k
        half = (arr[i] >> (halves + 1)) + half_not_half(i + 1, halves + 1)
        return max(not_half, half)

    print(half_not_half())
