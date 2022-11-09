from sys import stdin, stdout

n = int(stdin.readline().strip())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

roads = int(stdin.readline().strip())

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


for curr in range(roads):
    (a, b, w) = map(int, stdin.readline().split())

    a -= 1
    b -= 1

    matrix[b][a] = matrix[a][b] = min(matrix[a][b], w)

    for i in range(n):
        matrix[a][i] = matrix[i][a] = min(matrix[i][a], matrix[i][b] + matrix[b][a])

    for i in range(n):
        matrix[b][i] = matrix[i][b] = min(matrix[i][b], matrix[i][a] + matrix[b][a])

    summ = 0
    for i in range(n):
        for j in range(n - 1, i - 1, -1):
            matrix[i][j] = min(matrix[i][j], matrix[i][b] + matrix[b][j])
            summ += matrix[i][j]

    print(summ, end=" " if curr != roads - 1 else "\n")
