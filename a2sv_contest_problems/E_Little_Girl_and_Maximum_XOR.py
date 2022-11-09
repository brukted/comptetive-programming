from sys import stdin, stdout

a, b = map(int, stdin.readline().split())

ans = 0

for shift in range(66 - 1, -1, -1):
    if a & 1 << shift == b & 1 << shift:
        continue

    elif a & 1 << shift == 1 and b & 1 << shift == 0:
        ans += 1 << shift
        continue
    else:
        ans += (1 << (shift + 1)) - 1
        break

print(ans)
