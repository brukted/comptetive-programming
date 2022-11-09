from sys import stdin, stdout

calories = [0] + list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().strip()))
print(sum(map(calories.__getitem__, arr)))
