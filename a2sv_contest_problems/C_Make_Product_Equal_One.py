from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
moves = 0
prod = 1
zeros = 0

for i in arr:
    if i == 1 or i == -1:
        prod *= i
        continue
    if i == 0:
        zeros += 1
    elif i > 1:
        moves += i - 1
    else:
        moves += -1 - i
        prod *= -1

if prod == 1:
    moves += zeros
else:
    if zeros > 0:
        moves += zeros
    else:
        moves += 2
    
print(moves)
