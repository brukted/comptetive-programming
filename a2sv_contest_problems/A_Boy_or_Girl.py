from collections import Counter


count = Counter(input())

if len(count) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")