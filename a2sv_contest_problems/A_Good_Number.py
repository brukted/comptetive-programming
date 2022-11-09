n , k = map(int, input().split())

goods = 0
for _ in range(n):
    s = input()
    count = [0] * 10
    
    for ch in s:
       count[int(ch)] += 1
    isGood = True
    
    for c in range(k + 1):
        if count[c] == 0:
            isGood = False
            break
    goods += 1 if isGood else 0

print(goods)