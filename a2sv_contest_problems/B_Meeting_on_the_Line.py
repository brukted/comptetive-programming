from sys import stdin, stdout
t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    poses = list(map(int, stdin.readline().split()))
    times = list(map(int, stdin.readline().split()))
    print((min(poses) + max(poses) ) / 2)
