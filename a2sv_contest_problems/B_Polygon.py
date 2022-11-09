from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    matrix = []
    for _ in range(n):
        matrix.append(stdin.readline().strip())

    ans = True
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if matrix[i][j] == '0':
                continue
            if matrix[i][j + 1] != '1' and matrix[i + 1][j] != '1':
                ans = False
                break

    print('YES' if ans else 'NO')
