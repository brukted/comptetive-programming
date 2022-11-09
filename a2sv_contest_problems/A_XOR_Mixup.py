t = int(input())

for _ in range(t):
    _ = int(input())
    a = list(map(int, input().split()))

    val = 0

    for x in a:
        val ^= x
    
    for x in a:
        if x ^ val == x:
            print(x)
            break