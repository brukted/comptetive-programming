from cmath import inf
from collections import defaultdict
from sys import stdin, stdout

str = stdin.readline().strip()
max_diff = defaultdict(lambda: -inf)
last = defaultdict(lambda: -1)

for idx, ch in enumerate(str):
    max_diff[ch] = max(max_diff[ch], idx - last[ch])
    last[ch] = idx

for ch in max_diff.keys():
    max_diff[ch] = max(max_diff[ch], len(str)- last[ch])

print(min(max_diff.values()))
