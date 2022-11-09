from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, q = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    summ = evens_count = odds_count = 0

    for num in arr:
        summ += num
        
        if num % 2 == 0:
            evens_count += 1
        else:
            odds_count += 1

    for _ in range(q):
        typ, num = map(int, stdin.readline().split())

        if typ == 0: # evens 
            summ += num * evens_count
            
            if num % 2 == 1:
                odds_count += evens_count
                evens_count = 0
        else:
            summ += num * odds_count
            if num % 2 == 1:
                evens_count += odds_count
                odds_count = 0

        print(summ)
