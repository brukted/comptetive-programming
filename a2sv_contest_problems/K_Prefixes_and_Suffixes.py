from sys import stdin, stdout
from collections import Counter, defaultdict


def buildPrefix(pattern):
    prefix = [0] * len(pattern)
    i, j = 0, 1

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            prefix[j] = i + 1
            i, j = i + 1, j + 1
            continue
        if i == 0:
            prefix[j] = 0
            j += 1
        else:
            i = prefix[i - 1]

    return prefix


s = stdin.readline().strip()
lsp = buildPrefix(s)
count =  [1] * len(s)

for i in range(len(s) -1, 0, -1):
    count[lsp[i - 1]] += count[i]

cc = defaultdict(int)

for (mul, v) in zip(count, lsp):
    cc[v] += mul

proper_suffix_lens = []
i = len(s) - 1

while lsp[i] != 0:
    proper_suffix_lens.append(lsp[i])
    i = lsp[i - 1]
proper_suffix_lens.sort()

print(len(proper_suffix_lens) + 1)

for l in proper_suffix_lens:
    print(l, cc[l] + 1)

print(len(s), 1)
