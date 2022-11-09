from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

sum = 0
need = 0
last_height = 0

for idx, height in enumerate(arr):
    sum += last_height - height
    if sum < 0:
        need -= sum
        sum = 0
    last_height = height

print(need)
