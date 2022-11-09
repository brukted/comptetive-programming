t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    is_tall = [0] * n
    talls = 0

    less_than_left = None
    greater_than_right = None

    for i in range(1, n - 1):
        if a[i] > a[i-1] + a[i+1]:
            is_tall[i] = -1
            talls += 1
        else:
            is_tall[i] = a[i+1] + a[i-1] - a[i]

    can_be_taller = None

    for i in range(1, n - 1):
        if is_tall[i] != -1 and is_tall[i-1] != -1 and is_tall[i+1] != -1 and is_tall[i] < k:
            if can_be_taller is None:
                can_be_taller = i
            elif can_be_taller != i-1:
                can_be_taller = -1
                break

    if can_be_taller == -1:
        print(talls+2)
    else:
        print(talls)