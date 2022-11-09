t = int(input())

for _ in range(t):
    a , b = map(int, input().split())
    c = min(a, b)
    
    leftover = a - c if a > b else b - c
    leftover = leftover // 2 
    
    teams = min(leftover, c)
    
    c -= teams
    teams += c // 2

    print(teams)
    