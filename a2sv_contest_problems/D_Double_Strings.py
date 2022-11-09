t = int(input())

for _ in range(t):
    n = int(input())
    strings = []

    for _ in range(n):
        strings.append(input())

    hashed = set(strings)

    ans = []

    for string in strings:
        found = False
        for i in range(1, len(string)):
            if string[:i] in hashed and string[i:] in hashed:
                ans.append("1")
                found = True
                break
        if not found:
            ans.append("0")
    
    print(''.join(ans))
