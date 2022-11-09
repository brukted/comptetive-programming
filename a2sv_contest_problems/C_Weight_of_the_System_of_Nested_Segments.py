from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    stdin.readline()

    n, m = map(int, stdin.readline().split())

    arr = []

    for idx in range(m):
        x, w = map(int, stdin.readline().split())
        arr.append((x, w, idx + 1))

    arr.sort(key=lambda x: x[1])

    arr = sorted(arr[:n * 2])

    stdout.write(str(sum(map(lambda x: x[1], arr))))
    stdout.write('\n')
    # print(arr)

    for i in range(n):
        stdout.write(str(arr[i][2]))
        stdout.write(' ')
        stdout.write(str(arr[~i][2]))
        stdout.write('\n')
    
    stdout.write('\n')
