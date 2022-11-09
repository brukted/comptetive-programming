from collections import defaultdict
from email.policy import default


t = int(input())

words = {}

for _ in range(t):
    word = input()
    if word not in words:
        words[word] = 1
        print('OK')
    else:
        print(f"{word}{words[word]}")
        words[word] += 1
