from math import inf
from sys import stdin, stdout


def main():
    t = int(stdin.readline().strip())

    for _ in range(t):
        _, k = map(int, stdin.readline().split())
        arr = list(map(int, stdin.readline().split()))
        arr.sort()
        counts = []

        last = arr[0]
        c = 0
        for num in arr:
            if num == last:
                c += 1
            else:
                counts.append((last, c))
                last = num
                c = 1

        counts.append((last, c))

        l, r = inf, -inf
        i = 0
        j = 0

        while j < len(counts):
            while j < len(counts) and counts[j][1] >= k and (i == j or counts[j][0] == counts[j-1][0] + 1):
                j += 1

            if i != j and counts[j - 1][0] - counts[i][0] > r - l:
                l, r = counts[i][0], counts[j-1][0]

            i = j
            while i < len(counts) and counts[i][1] < k:
                i += 1

            j = i

        if r < l:
            stdout.write(str(-1))
            stdout.write('\n')
        else:
            stdout.write(str(l))
            stdout.write(' ')
            stdout.write(str(r))
            stdout.write('\n')


main()
