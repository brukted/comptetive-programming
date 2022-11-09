from sys import stdin, stdout


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
middles = set(lsp[1:-1])

# ans = 
i = len(s) - 1
while lsp[i] not in middles and lsp[i] != 0:
    i = lsp[i - 1]

if lsp[i] == 0:
    print("Just a legend")
else:
    print(s[:lsp[i]])

