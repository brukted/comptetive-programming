from sys import stdin


def sng_int(): return int(stdin.readline())
def sng_str(): return stdin.readline()
def int_list(): return list(map(int, stdin.readline().split()))


t = sng_int()

for _ in range(t):
    n, s = map(int, sng_str().split())
    arr = int_list()
    i = 0
    j = 0
    l, r = 0, -1

    while j < n:
        while j < n and s + arr[j] >= 0:
            s += arr[j]
            j += 1

        if j - i > r - l:
            l = i
            r = j

        if j < n:
            while i <= j and s + arr[j] < 0:
                s -= arr[i]
                i += 1

    if l + 1 <= r:
        print(l + 1, r)
    else:
        print('-1')
