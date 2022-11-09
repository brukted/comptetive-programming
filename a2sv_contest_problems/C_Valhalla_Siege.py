from sys import prefix, stdin, stdout

n, q = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
k_arr = list(map(int, stdin.readline().split()))

pre_sum = []
prefix = 0
for num in arr:
    prefix += num
    pre_sum.append(prefix)

s_sum = pre_sum[-1]
k_sum = 0


def solve(val, arr):
    l, r = 0, len(arr) - 1
    best = -1

    while l <= r:
        mid = (l + r) // 2
        m_val = arr[mid]

        if m_val <= val:
            best = mid
            l = mid + 1
        else:
            r = mid - 1

    return best


for ki in k_arr:
    k_sum += ki

    if k_sum >= s_sum:
        k_sum = 0

    print(n - solve(k_sum, pre_sum) - 1)
