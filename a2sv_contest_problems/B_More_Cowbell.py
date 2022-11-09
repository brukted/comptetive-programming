from math import inf


def boxes(cap, arr):
    i = 0
    j = len(arr) - 1
    ans = 0

    while i <= j:
        if arr[j] + arr[i] > cap:
            if arr[j] > cap:
                return inf
            ans += 1
            j -= 1
        else:
            i += 1
            j -= 1
            ans += 1

    return ans


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    l = max(arr)
    r = 0

    if n > 1:
        r = arr[-1] + arr[-2]
    else:
        r = arr[-1]

    best = None

    while l <= r:
        mid = l + (r - l) // 2
        bb = boxes(mid, arr)

        if bb > k:
            l = mid + 1
        else:
            r = mid - 1
            best = mid

    print(best)


main()
