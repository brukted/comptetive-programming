from cmath import inf
from collections import Counter
from sys import stdin, stdout


t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))

    count_of_counts = list(Counter(arr).values())

    count_of_counts = list(Counter(count_of_counts).items())

    count_of_counts.sort(reverse=True)

    ans = 0
    last = 10 ** 6

    for (c, cc) in count_of_counts:

        if c >= last:
            begin = last - 1
        else:
            begin = c
        
        p = 0
        while p != cc and begin != 0:
            ans += begin
            last = begin
            p += 1
            begin -= 1
        
    print(ans)
