from sys import stdin, stdout

s = stdin.readline().strip()

for idx, ch in enumerate(s):
    if ch.islower():
        print(sum(map(lambda ch: ch.isupper(), s[idx:])))
        exit()

print(0)
