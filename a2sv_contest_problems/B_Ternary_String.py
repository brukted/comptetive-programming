t = int(input())

for _ in range(t):
    s = list(input())

    count = [0] * 4

    i, j = 0, 0

    l = float("inf")

    def is_valid(): return count[1] > 0 and count[2] > 0 and count[3] > 0

    while j < len(s):
        while j < len(s) and not is_valid():
            count[int(s[j])] += 1
            j += 1

        while i < j and is_valid():
            l = min(l, j - i)

            count[int(s[i])] -= 1
            i += 1

    if l == float("inf"):
        print("0")
    else:
        print(l)
