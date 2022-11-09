s = input()


m = 0
curr = 1
prev = s[0]

for i in range(1,len(s)):
    if prev == s[i]:
        curr += 1
    else:
        m = max(m, curr)
        curr = 1
   
    prev = s[i]

m = max(m, curr)

if m >= 7:
    print('YES')
else:
    print('NO')
