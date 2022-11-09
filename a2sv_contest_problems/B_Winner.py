from collections import defaultdict


score  = defaultdict(int)

n = int(input())

score_changes = []

for i in range(n):
    name , delta = input().split()
    score[name] += int(delta)
    score_changes.append((name , int(delta)))

m = max(score.values())

candidates = set(filter(lambda x : score[x] == m, list(score.keys())))

new_score = defaultdict(int)

for name, delta in score_changes:
    new_score[name] += delta
    if new_score[name] >= m and name in candidates:
        print(name)
        exit()
