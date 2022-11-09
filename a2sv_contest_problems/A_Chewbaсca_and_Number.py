from sys import stdin, stdout

arr = list(map(int, list(input())))

for idx, num in enumerate(arr):
    if 9 - num < num and (not (idx == 0 and 9 - num == 0)):
        arr[idx] = 9 - num

print("".join(map(str, arr)))