n, t = map(int, input().split())

que = list(input())

res = []
girls = 0

for idx, ch in enumerate(que):
    if ch =='G' and girls < t:
        girls += 1
    else:
        res.append(ch)

res = ['G'] * girls + res

print(''.join(res))