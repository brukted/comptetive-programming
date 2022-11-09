
from collections import Counter
from sys import stdin, stdout


n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr.sort()
cont = list(Counter(arr).items())
ans = sum(map(lambda x: x[1] if x[0] !=
          arr[0] and x[0] != arr[-1] else 0, cont))
print(ans)
