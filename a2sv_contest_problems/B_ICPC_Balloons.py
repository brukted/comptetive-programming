t = int(input())

for _ in range(t):
    _ = int(input())
    s = input()
    balloons = 0
    
    seen = set()

    for ch in s:
        if ch in seen:
            balloons += 1
        else:
            seen.add(ch)
            balloons += 2
    
    print(balloons)
