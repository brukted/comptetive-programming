from sys import stdin, stdout

n, k = map(int, stdin.readline().split())

s = stdin.readline().strip()

count = {'a': 0, 'b': 0}

ans = j = 0

for i in range(n):
    while j < n and min(count['a'], count['b']) <= k:
        ans = max(ans, j - i)
        count[s[j]] += 1
        j += 1
    
    if j == n:
        ans = max(ans, j - i)
        break
    
    count[s[i]] -= 1

print(ans)
