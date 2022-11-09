from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    array = list(map(int, stdin.readline().split()))
    string = stdin.readline().strip()
    mapping = {}
    match = True

    for idx in range(n):
        if array[idx] in mapping:
            if string[idx] != mapping[array[idx]]:
                match = False
                break
        else:
            mapping[array[idx]] = string[idx]

    print('YES' if match else 'NO')