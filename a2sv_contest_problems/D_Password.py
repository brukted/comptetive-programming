def build_lsp(pattern):
    lsp = [0] * len(pattern)
    i, j = 0, 1

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            lsp[j] = i + 1
            i, j = i + 1, j + 1
            continue

        if i == 0:
            lsp[j] = 0
            j += 1
        else:
            i = lsp[i - 1]
    return lsp


s = input()
lsp = build_lsp(s)
print(lsp)
