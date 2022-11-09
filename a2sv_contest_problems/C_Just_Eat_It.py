from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())

    arr = list(map(int, stdin.readline().split()))
    ss = sum(arr)

    min_prefix = 0
    happy = True
    prefix = 0

    for i in arr[:-1]:
        prefix += i

        if prefix - min_prefix >= ss:
            happy = False
            break

        min_prefix = min(min_prefix, prefix)
    
    if happy:
        min_prefix = 0
        happy = True
        prefix = 0

        for i in arr[1:]:
            prefix += i

            if prefix - min_prefix >= ss:
                happy = False
                break

            min_prefix = min(min_prefix, prefix)

    print('YES' if happy else 'NO')
